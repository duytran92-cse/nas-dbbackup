
import gzip

from notasquare.urad_api import *
from application.models import *
from application.settings import dev as settings
from . import components
import os, sys, time

import boto
import boto.s3.connection

class Create(handlers.standard.CreateHandler):
    def parse_and_validate(self, params):
        parser = self.container.create_parser(params)
        if not parser.parse('bucket_create', 'string'):
            self.add_error('bucket_create', 'MUST_NOT_BE_EMPTY')
        return parser.get_data()
        #---> fixing crud.py
    def create(self, data):
        connect = boto.connect_s3(aws_access_key_id = settings.AWS_ACCESS_KEY_ID,
                                aws_secret_access_key = settings.AWS_SECRET_ACCESS_KEY,
                                calling_format = boto.s3.connection.OrdinaryCallingFormat())
        bucket = connect.create_bucket(data['bucket_create'])
        return bucket