# Generated by Django 2.1.7 on 2019-04-24 11:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [('openwisp_users', '0005_user_phone_number')]

    operations = [
        migrations.AlterIndexTogether(name='user', index_together={('id', 'email')})
    ]
