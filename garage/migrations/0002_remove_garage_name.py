# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-23 15:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='garage',
            name='name',
        ),
    ]
