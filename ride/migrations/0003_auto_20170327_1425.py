# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-27 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0002_auto_20170327_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
