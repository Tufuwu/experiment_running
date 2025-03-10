# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-04 13:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("a4ratings", "0002_use_usergenerated_content_base_model"),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name="rating",
            index_together=set([("content_type", "object_pk")]),
        ),
    ]
