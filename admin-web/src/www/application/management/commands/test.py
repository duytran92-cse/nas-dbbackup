from django.core.management.base import BaseCommand#, CommandError
from django.utils import timezone
#from notasquare.urad_api.containers.standard import Container
#from application.models import *
from django.conf import settings
import os, sys, time

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
    	filestamp = time.strftime('%Y-%m-%d-%I:%M')
    	os.system("mysqldump -h %s -P %s -u%s -p%s %s | gzip > %s.sql.gz" %('172.17.0.2', 3306, 'root', 123456, 'api_db', 'api_db' + '_' + filestamp))
	print 'dump done'
    	# os.system('ping 172.17.0.2')
    	# print filestamp
