# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 10:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('garage', '0022_auto_20170327_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleRide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_location_lat', models.FloatField()),
                ('start_location_lng', models.FloatField()),
                ('start_location_city', models.CharField(max_length=120)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('allow_bikers_join', models.BooleanField(default=False)),
                ('bicycle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.Bicycle')),
                ('motorcycle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='garage.Motorcycle')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleRideMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule_ride.ScheduleRide')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='scheduleride',
            name='user',
            field=models.ManyToManyField(through='schedule_ride.ScheduleRideMembership', to=settings.AUTH_USER_MODEL),
        ),
    ]
