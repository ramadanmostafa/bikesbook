# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-23 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garage', '0002_remove_garage_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BicyceStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='BicycleMake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='bicycle',
            name='color',
        ),
        migrations.AlterField(
            model_name='bicycle',
            name='make',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='garage.BicycleMake'),
        ),
        migrations.AddField(
            model_name='bicycle',
            name='style',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='garage.BicyceStyle'),
            preserve_default=False,
        ),
    ]