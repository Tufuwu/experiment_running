# Generated by Django 2.2.10 on 2020-02-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("a4_candy_debate", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="description",
            field=models.CharField(
                blank=True,
                help_text="In addition to the title, you can insert an optional explanatory text. This field is only shown in the participation if it is filled out",
                max_length=320,
                verbose_name="Description",
            ),
        ),
    ]
