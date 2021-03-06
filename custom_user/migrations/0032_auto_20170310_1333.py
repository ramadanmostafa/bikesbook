# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-10 13:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_user', '0031_auto_20170225_2326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField()),
                ('lang', models.FloatField()),
                ('is_break', models.BooleanField(default=False)),
                ('time', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='ride',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='custom_user.Ride'),
        ),
    ]
