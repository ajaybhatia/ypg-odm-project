# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-29 03:11
from __future__ import unicode_literals

from django.db import migrations, models
import odm_builder.models


class Migration(migrations.Migration):

    dependencies = [
        ('odm_builder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='source_file',
            field=models.FileField(storage=odm_builder.models.MediaFileSystemStorage(), upload_to=''),
        ),
    ]
