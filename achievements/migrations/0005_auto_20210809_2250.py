# Generated by Django 2.2.15 on 2021-08-09 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0004_achievementitemlink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievementitemlink',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
