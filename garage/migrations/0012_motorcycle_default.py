# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-22 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0011_bicycle_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorcycle',
            name='default',
            field=models.BooleanField(default=False),
        ),
    ]