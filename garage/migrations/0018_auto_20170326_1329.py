# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-26 11:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0017_motorcyclenew'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BicycleNew',
            new_name='NewBicycle',
        ),
        migrations.RenameModel(
            old_name='MotorcycleNew',
            new_name='NewMotorcycle',
        ),
    ]
