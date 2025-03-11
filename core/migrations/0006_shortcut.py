# Generated by Django 2.2.25 on 2022-02-18 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_extendeduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shortcut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('location', models.CharField(max_length=32, unique=True)),
                ('reference_url', models.URLField()),
            ],
        ),
    ]
