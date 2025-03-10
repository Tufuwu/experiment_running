# Generated by Django 3.1.5 on 2021-01-09 16:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("command_log", "0002_add_error_to_log"),
    ]

    operations = [
        migrations.AddField(
            model_name="managementcommandlog",
            name="truncate_at",
            field=models.DateTimeField(
                blank=True,
                help_text="Timestamp after which record can be safely deleted.",
                null=True,
            ),
        ),
    ]
