# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-21 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170330_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Name of User'),
        ),
    ]
