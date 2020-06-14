from django.core.management.base import BaseCommand#, CommandError
from django.utils import timezone
from notasquare.urad_api.containers.standard import Container
from application.models import *
from django.conf import settings
# import os, sys, time, boto, boto3
# from boto.s3.key import Key
import os, sys
import MySQLdb

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		host = '172.17.0.2'
		port = '3306'
		user ='root'
		password = '123456'
		databasename = 'api1_db'
		print '----> begin test'
		db_connect = MySQLdb.connect(host, user, password)
		cursor = db_connect.cursor()
		query_count = cursor.execute('select count(*) from information_schema.tables where table_schema = "%s"' %(databasename))
		#cursor.execute('CREATE DATABASE %s' %(databasename))
		#os.system('mysql -h %s -P %s -u%s -p%s %s < %s' %(host, port, user, password, databasename, databasename + '.sql'))
		#if int(query_count == 0:
		#print cursor.fetchone()
		if cursor.fetchone() == (0L,):
		   print 'yesy'
		db_connect.close()
		print 'done'
