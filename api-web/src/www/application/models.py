from __future__ import unicode_literals
from django.db import models
from . import constants

class DatabaseBackup(models.Model):
    db_url = models.CharField(max_length=255)
    db_port = models.CharField(max_length=255)
    db_username = models.CharField(max_length=255)
    db_password = models.CharField(max_length=255)
    db_name = models.CharField(max_length=255)
    db_time = models.CharField(max_length=255)
    db_code = models.CharField(max_length=255)
    aws_bucket = models.CharField(max_length=255)
    aws_filename = models.CharField(max_length=255)

class DatabaseRestore(models.Model):
    db_name = models.CharField(max_length=255)
    db_code = models.CharField(max_length=255)
    aws_bucket = models.CharField(max_length=255)
    aws_filename = models.CharField(max_length=255)
    restore_time = models.CharField(max_length=255)
    is_override = models.CharField(max_length=10)           
