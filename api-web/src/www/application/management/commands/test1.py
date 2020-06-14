from django.core.management.base import BaseCommand#, CommandError
from django.utils import timezone
from notasquare.urad_api.containers.standard import Container
from application.models import *
from django.conf import settings
import os, sys, time, boto, boto3
from boto.s3.key import Key

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		# client = boto3.client('s3', aws_access_key_id='AKIAINK6TVPLDQ4R6YQA', aws_secret_access_key='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')
		# # bucket_name = "api_db_test"
		# s3=boto3.resource('s3')
		# # s3.upload_file("api_db_dump.sql.gz", bucket_name, filename.split('/')[len(filename.split('/'))-1])
		# data = open('test1.sql.gz', 'rb')
		# s3.Bucket('api_db_test').put_object(Key='test2.jpg', Body=data)
		# # print 'hello'
		AWS_ACCESS_KEY_ID = 'AKIAINK6TVPLDQ4R6YQA'
		AWS_SECRET_ACCESS_KEY = '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'
		
		fileName="performance_schema_2017-05-12-07:44.sql.gz"
		bucketName="api_db_test"

		file=open(fileName)

		conn = boto.connect_s3(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
		bucket = conn.get_bucket(bucketName)
		k = Key(bucket)
		k.key=fileName
		result = k.set_contents_from_file(file)