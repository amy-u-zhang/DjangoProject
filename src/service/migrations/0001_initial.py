# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Temperatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.IntegerField(default=None, null=True)),
                ('longitute', models.IntegerField(default=None, null=True)),
                ('noaa', models.FloatField(default=None, null=True)),
                ('weather_com', models.FloatField(default=None, null=True)),
                ('accuweather', models.FloatField(default=None, null=True)),
                ('average', models.FloatField(default=None, null=True)),
            ],
        ),
    ]
