# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 14:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule_ride', '0005_auto_20170402_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduleridejoiningrequests',
            name='to_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL),
        ),
    ]