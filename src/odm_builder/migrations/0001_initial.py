# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 10:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soc_vendor', models.CharField(choices=[('MediaTek', 'MTK'), ('QualComm', 'QCOM'), ('Spreadtrum', 'Spreadtrum')], default='MediaTek', max_length=20)),
                ('odm', models.CharField(choices=[('Tinno', 'Tinno'), ('Huaqin', 'Huaqin'), ('IMG', 'IMG'), ('Ragentek', 'Ragentek'), ('Wingtech', 'Wingtech'), ('Coolpad', 'Coolpad'), ('Amer', 'Amer'), ('Sprocomm', 'Sprocomm'), ('Topwisez', 'Topwisez')], default='Tinno', max_length=20)),
                ('android_version', models.CharField(choices=[('L-5.1.1', 'L-5.1.1'), ('M-6.0', 'M-6.0'), ('M-6.0.1', 'M-6.0.1'), ('N-7.0', 'N-7.0')], default='L-5.1.1', max_length=20)),
                ('build_type', models.CharField(choices=[('OTA', 'OTA'), ('Factory', 'Factory')], default='OTA', max_length=10)),
                ('source_file', models.FileField(upload_to='')),
                ('buildprop_file', models.FileField(upload_to='')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]