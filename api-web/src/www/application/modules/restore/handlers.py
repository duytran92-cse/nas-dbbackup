
from notasquare.urad_api import *
from application.models import *
from application.settings import dev as settings
from . import components
import MySQLdb
import os, sys, time, boto, boto3
from boto.s3.key import Key

class List(handlers.standard.ListHandler):
    #query restore database from database
    def create_query(self, data):
        query = DatabaseRestore.objects
        if 'name' in data:
            query = query.filter(name__contains=data['name'])
        return query
    #return json format
    def serialize_entry(self, database):
        return {
            'id': database.id,
            'name': database.db_name,
            'aws_bucket': database.aws_bucket,
            'aws_filename': database.aws_filename,
            'time': database.restore_time,
            'code': database.db_code,
            'is_override': database.is_override
        }

class Create(handlers.standard.CreateHandler):
    def parse_and_validate(self, params):
        parser = self.container.create_parser(params)
        if not parser.parse('database_name', 'string'):
            self.add_error('database_name', 'MUST_NOT_BE_EMPTY')
        return parser.get_data()
    def create(self, data):
        filestamp = time.strftime('%Y-%m-%d-%I:%M')
        database = DatabaseRestore()
        database.aws_bucket = data['aws_bucket']
        database.aws_filename = data['aws_filename']
        print data['aws_filename']
        database.db_name = data['database_name']
        database.restore_time = filestamp
        database.db_code = data['database_name'] + '_' + filestamp
        if data['is_override'] == 'on':
            database.is_override = 'true'
        else:
            database.is_override = 'false'
        database.save()
        print '----> save to database done'

        conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        bucket = conn.get_bucket(data['aws_bucket'])
        k = Key(bucket, data['aws_filename'] + '.sql')
        k.get_contents_to_filename(data['aws_filename'] + '.sql')
        print '-----> download done'

        print '---> begin load database'
        db_connect = MySQLdb.connect(data['database_url'], data['database_username'], data['database_password'])
        cursor = db_connect.cursor()
        #check the database exists or not in database
        query_count = cursor.execute('SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = "%s"' %(data['database_name']))
        print query_count

        host = data['database_url']
        port = data['database_port']
        user = data['database_username']
        password = data['database_password']
        sql_file = data['aws_filename'] + '.sql'
        databasename = data['database_name']

        #create new database and run sql script if database doesn't exist
        if cursor.fetchone() == (0L,):
            cursor.execute('CREATE DATABASE IF NOT EXISTS %s' %(databasename))
            os.system('mysql -h %s -P %s -u%s -p%s %s < %s' %(host, port, user, password, databasename, data['aws_filename'] + '.sql'))
        else:
            if data['is_override'] != 'on':
                print 'override database is not allowed ---> do nothing'
            else:
                print 'override database is allowed'
            # #drop old database + create new database
            # cursor.execute('DROP DATABASE IF EXISTS %s' %(databasename))
            # cursor.execute('CREATE DATABASE IF NOT EXISTS %s' %(databasename))            
            # os.system('mysql -h %s -P %s -u%s -p%s %s < %s' %(host, port, user, password, databasename, databasename + '.sql'))
            
        #move sql script to mysql backup => set /opt/bin/mysql_load in dev.py
        # os.system('mv %s /opt/bin/mysql_load' %(database_name + '.sql'))
        os.system('mv %s %s' %(sql_file, settings.RESTORE_DIR))
        return database
