# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-25 23:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0030_auto_20170225_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
