# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-27 11:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0021_auto_20170327_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='bicycle',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='motorcycle',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='user',
        ),
        migrations.DeleteModel(
            name='Ride',
        ),
    ]