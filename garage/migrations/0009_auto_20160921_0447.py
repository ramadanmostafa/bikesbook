# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-21 04:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0008_auto_20160921_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bicycle',
            name='make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garage.BicycleMake'),
        ),
    ]
