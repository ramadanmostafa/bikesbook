# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-31 19:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=120)),
                ('color', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('bicycles', models.ManyToManyField(blank=True, null=True, to='garage.Bicycle')),
            ],
        ),
        migrations.CreateModel(
            name='Motorcycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=120)),
                ('model', models.CharField(max_length=120)),
                ('color', models.CharField(max_length=120)),
                ('year', models.IntegerField()),
                ('engine_size', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='garage',
            name='motorcycles',
            field=models.ManyToManyField(blank=True, null=True, to='garage.Motorcycle'),
        ),
        migrations.AddField(
            model_name='garage',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]