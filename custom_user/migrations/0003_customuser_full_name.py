# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-25 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0002_auto_20160725_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]