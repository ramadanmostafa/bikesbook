# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-12 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0037_auto_20170311_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='lat',
            new_name='end_lat',
        ),
        migrations.RenameField(
            model_name='ride',
            old_name='lng',
            new_name='end_lng',
        ),
        migrations.AddField(
            model_name='ride',
            name='end_time',
            field=models.IntegerField(default=5456),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ride',
            name='start_lat',
            field=models.FloatField(default=5465),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ride',
            name='start_lng',
            field=models.FloatField(default=45.4545),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ride',
            name='start_time',
            field=models.IntegerField(default=12.526565635),
            preserve_default=False,
        ),
    ]