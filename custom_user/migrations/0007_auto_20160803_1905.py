# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-03 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0006_auto_20160803_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='country_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
