# Generated by Django 2.1.5 on 2019-03-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("roles", "0009_bodyrole_official_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="bodyrole",
            name="permanent",
            field=models.BooleanField(default=False),
        ),
    ]
