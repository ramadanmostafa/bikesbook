# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-25 22:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0026_auto_20170225_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='share_my_info',
            new_name='share_my_info_using',
        ),
        migrations.AlterField(
            model_name='settings',
            name='distance_unit',
            field=models.CharField(default=b'km', max_length=60),
        ),
        migrations.AlterField(
            model_name='settings',
            name='gps_acc',
            field=models.CharField(default=b'30', max_length=60),
        ),
        migrations.AlterField(
            model_name='settings',
            name='publish_time_interval',
            field=models.CharField(default=b'30', max_length=60),
        ),
    ]