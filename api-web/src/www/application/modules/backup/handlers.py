
from notasquare.urad_api import *
from application.models import *
from application.settings import dev as settings
from . import components
import os, sys, time, boto, boto3
from boto.s3.key import Key
from boto3.session import Session

class List(handlers.standard.ListHandler):
    #query backup database from database
    def create_query(self, data):
        query = DatabaseBackup.objects
        if 'database_name' in data:
            query = query.filter(name__contains=data['database_name'])
        return query
    #return json output
    def serialize_entry(self, database):
        return {
            'id': database.id,
            'name': database.db_name,
            'port': database.db_port,
            'username': database.db_username,
            'url':database.db_url,
            'password': database.db_password,
            'time': database.db_time,
            'aws_bucket': database.aws_bucket,
	    'aws_filename': database.aws_filename,
            'code': database.db_code
        }


class Create(handlers.standard.CreateHandler):
    def parse_and_validate(self, params):
        parser = self.container.create_parser(params)
        if not parser.parse('database_url', 'string'):
            self.add_error('database_url', 'MUST_NOT_BE_EMPTY')
        if not parser.parse('database_port', 'string'):
            self.add_error('database_port', 'MUST_NOT_BE_EMPTY')
        if not parser.parse('database_username', 'string'):
            self.add_error('database_username', 'MUST_NOT_BE_EMPTY')
        if not parser.parse('database_password', 'string'):
            self.add_error('database_password', 'MUST_NOT_BE_EMPTY')
        if not parser.parse('database_name', 'string'):
            self.add_error('database_name', 'MUST_NOT_BE_EMPTY')
        if not parser.parse('aws_bucket', 'string'):
            self.add_error('aws_bucket', 'MUST_NOT_BE_EMPTY')
        if not parser.parse('aws_filename', 'string'):
            self.add_error('aws_filename', 'MUST_NOT_BE_EMPTY')
        return parser.get_data()
    def create(self, data):
        filestamp = time.strftime('%Y-%m-%d-%I:%M')
        os.system("mysqldump -h %s -P %s -u%s -p%s %s > %s.sql" %(data['database_url'], data['database_port'], data['database_username'], data['database_password'], data['database_name'], data['database_name']))
        database = DatabaseBackup()
        database.aws_bucket = data['aws_bucket']
        database.aws_filename = data['aws_filename']
        database.db_url = data['database_url']
        database.db_port = data['database_port']
        database.db_username = data['database_username']
        database.db_password = data['database_password']
        database.db_name = data['database_name']
        database.db_time = filestamp
        database.db_code = data['database_name'] + '_' + filestamp
        database.save()

        print '---> dump + write logs OK'

        s3_session = Session(aws_access_key_id = settings.AWS_ACCESS_KEY_ID, aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY)
        _s3 = s3_session.resource('s3')
        local_file = open(data['database_name'] + '.sql', 'rb')
        _s3.Bucket(data['aws_bucket']).put_object(Key=data['aws_filename'] + '.sql', Body=local_file)
        print '---> upload done'

        # fileName= data['database_name'] + '.sql'
        # bucketName=data['aws_bucket']
        # file=open(fileName)
        # conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
        # bucket = conn.get_bucket(bucketName)
        # k = Key(bucket)
        # k.key=fileName
        # result = k.set_contents_from_file(file)


        #move backup file to /opt/bin/mysql_backup
        os.system('mv %s %s' %(data['database_name'] + '.sql', settings.BACKUP_DIR))
        print '----> move database done'
        return database
