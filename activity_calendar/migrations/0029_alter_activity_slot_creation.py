# Generated by Django 4.1.13 on 2024-10-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activity_calendar", "0028_remove_activity_is_public"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="slot_creation",
            field=models.CharField(
                choices=[
                    ("CREATION_STAFF", "By Organisers"),
                    ("CREATION_AUTO", "Automatically"),
                    ("CREATION_USER", "By Users"),
                    ("CREATION_NONE", "No signup"),
                ],
                default="CREATION_NONE",
                max_length=15,
            ),
        ),
    ]
