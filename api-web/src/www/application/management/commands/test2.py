from django.core.management.base import BaseCommand#, CommandError
from django.utils import timezone
from notasquare.urad_api.containers.standard import Container
from application.models import *
from django.conf import settings
import os, sys, time, boto, boto3
from boto.s3.key import Key

class Command(BaseCommand):
	def handle(self, *args, **kwargs):
		conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID,settings.AWS_SECRET_ACCESS_KEY)
		bucket = conn.get_bucket('api_db_test')
		# print bucket
		k = Key(bucket,'api_db_2017-05-13-01:43.sql.gz')
		k.get_contents_to_filename('test.gz')
		os.system('mv test.gz /opt/bin/mysql_load/')