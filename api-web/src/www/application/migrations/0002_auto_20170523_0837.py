# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-05-23 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='databaserestore',
            old_name='aws_filename',
            new_name='aws_bucket',
        ),
    ]