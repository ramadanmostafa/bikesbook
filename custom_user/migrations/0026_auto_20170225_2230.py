# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-25 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0025_auto_20170218_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Allow_bikers_join', models.BooleanField(default=False)),
                ('get_sos_notifications', models.BooleanField(default=False)),
                ('gps_acc', models.CharField(max_length=60)),
                ('distance_unit', models.CharField(max_length=60)),
                ('connect_with_fb', models.BooleanField(default=False)),
                ('connect_with_twitter', models.BooleanField(default=False)),
                ('publish_time_interval', models.CharField(max_length=60)),
                ('share_my_info', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='setting',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom_user.Settings'),
        ),
    ]
