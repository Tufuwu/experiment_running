# Generated by Django 2.0.5 on 2018-06-19 12:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roles", "0006_auto_20180401_2303"),
    ]

    operations = [
        migrations.AddField(
            model_name="bodyrole",
            name="priority",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
