# Generated by Django 3.1.12 on 2021-12-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("achievements", "0011_interest_userinterest"),
    ]

    operations = [
        migrations.AlterField(
            model_name="interest",
            name="title",
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
