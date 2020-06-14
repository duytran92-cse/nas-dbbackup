from django.core.management.base import BaseCommand#, CommandError
from django.utils import timezone
from notasquare.urad_api.containers.standard import Container
from application.models import *
from django.conf import settings
import os, sys, time, boto, boto3
import tinys3
from boto.s3.connection import S3Connection

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
    	# filestamp = time.strftime('%Y-%m-%d-%I:%M')
		  os.system("mysqldump -h %s -P %s -u%s -p%s %s | gzip > %s.sql.gz" %('172.17.0.2', 3306, 'root', 123456, 'api_db', 'api_db_dump'))
      client = boto3.client('s3', aws_access_key_id='AKIAINK6TVPLDQ4R6YQA', aws_secret_access_key='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')
      bucket_name = 'Nas-test'

      s3.upload_file(filename, bucket_name, filename.split('/')[len(filename.split('/'))-1])

        # client = boto3.client('s3', aws_access_key_id='AKIAINK6TVPLDQ4R6YQA', aws_secret_access_key='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')
        