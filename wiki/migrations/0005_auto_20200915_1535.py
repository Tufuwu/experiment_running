# Generated by Django 3.0.9 on 2020-09-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_auto_20200915_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('p', 'Projets'), ('n', 'Nourriture'), ('d', 'Divers'), ('o', 'Objets'), ('h', 'Hackerspace')], max_length=1),
        ),
        migrations.AlterField(
            model_name='historicalarticle',
            name='category',
            field=models.CharField(choices=[('p', 'Projets'), ('n', 'Nourriture'), ('d', 'Divers'), ('o', 'Objets'), ('h', 'Hackerspace')], max_length=1),
        ),
    ]
