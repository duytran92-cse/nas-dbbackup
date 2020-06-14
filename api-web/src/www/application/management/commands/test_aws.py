from django.core.management.base import BaseCommand#, CommandError
from django.utils import timezone
from notasquare.urad_api.containers.standard import Container
from application.models import *
from django.conf import settings
import os, sys, time, boto, boto3
from boto.s3.key import Key
from application.settings import dev as settings
from boto3.session import Session

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		print '---> begin upload database'
		# conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)

		# bucket = conn.get_bucket('api_db_test')
		# file = open('test_database.sql')
		
		# k = Key(bucket)
		# k.key = file

		# result = k.set_contents_from_file(file)
		# # result = k.set_contents_from_filename('blablabla.sql', headers=None, replace=True, cb=None, num_cb=10, policy=None, md5=None, reduced_redundancy=False, encrypt_key=False)

		s3_session = Session(aws_access_key_id = settings.AWS_ACCESS_KEY_ID, aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY)
		_s3 = s3_session.resource('s3')
		data = open('test_database.sql', 'rb')
		_s3.Bucket('api_db_test').put_object(Key='test1.sql', Body=data)

		# _bucket = _s3.Bucket('api_db_test')
		# _bucket.download_file(Key='test_db.sql', Filename='demo.sql')