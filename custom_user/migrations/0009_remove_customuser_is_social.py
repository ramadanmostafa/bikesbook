# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-03 19:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0008_auto_20160803_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_social',
        ),
    ]
