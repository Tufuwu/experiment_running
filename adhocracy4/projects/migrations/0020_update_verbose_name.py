# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-25 10:30
from __future__ import unicode_literals

import adhocracy4.projects.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("a4projects", "0019_rename_topic_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="topics",
            field=adhocracy4.projects.fields.TopicField(
                blank=True, default="", max_length=254, verbose_name="Project topics"
            ),
        ),
    ]
