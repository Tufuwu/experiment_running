# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("elections", "0005_auto_20170823_1648")]

    operations = [
        migrations.AlterField(
            model_name="candidacy",
            name="party",
            field=models.ForeignKey(
                help_text="Reference to the Organization representing the political party that nominated the candidate or would nominate the candidate (as in the case of a partisan primary).", # noqa
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="candidacies",
                to="core.Organization",
            ),
        ),
        migrations.AlterField(
            model_name="candidatecontest",
            name="party",
            field=models.ForeignKey(
                help_text="If the contest is among candidates of the same political party, e.g., a partisan primary election, reference to the Organization representing that party.", # noqa
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="candidate_contests",
                to="core.Organization",
            ),
        ),
        migrations.AlterField(
            model_name="election",
            name="administrative_organization",
            field=models.ForeignKey(
                help_text="Reference to the Organization that administers the election.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="elections",
                to="core.Organization",
            ),
        ),
        migrations.AlterField(
            model_name="election",
            name="division",
            field=models.ForeignKey(
                help_text="Reference to the Division that defines the broadest political geography of any contest to be decided by the election.", # noqa
                on_delete=django.db.models.deletion.PROTECT,
                related_name="elections",
                to="core.Division",
            ),
        ),
    ]
