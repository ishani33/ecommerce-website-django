# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-27 10:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20181227_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
