# Generated by Django 3.2.19 on 2024-03-14 12:05

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):
    dependencies = [
        ("a4_candy_activities", "0002_ckeditor_iframes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="description",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Description"),
        ),
    ]
