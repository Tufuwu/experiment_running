# Generated by Django 2.0.2 on 2018-03-06 11:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0014_auto_20180306_1632"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="followers",
            field=models.ManyToManyField(
                blank=True,
                related_name="followed_events",
                through="events.UserEventStatus",
                to="users.UserProfile",
            ),
        ),
        migrations.AlterField(
            model_name="usereventstatus",
            name="event",
            field=models.ForeignKey(
                default=uuid.uuid4,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ues",
                to="events.Event",
            ),
        ),
        migrations.AlterField(
            model_name="usereventstatus",
            name="user",
            field=models.ForeignKey(
                default=uuid.uuid4,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ues",
                to="users.UserProfile",
            ),
        ),
    ]
