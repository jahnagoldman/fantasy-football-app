# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playerdata', '0004_auto_20170113_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerrawstats',
            name='dateStat',
            field=models.DateField(verbose_name='date of stat'),
        ),
    ]
