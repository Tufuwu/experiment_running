# Generated by Django 3.2.19 on 2023-07-18 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("a4projects", "0039_add_alt_text_to_field"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("a4_candy_projects", "0004_verbose_name_created_modified"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProjectInsight",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="Created",
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, editable=False, null=True, verbose_name="Modified"
                    ),
                ),
                ("comments", models.PositiveIntegerField(default=0)),
                ("ratings", models.PositiveIntegerField(default=0)),
                ("written_ideas", models.PositiveIntegerField(default=0)),
                ("poll_answers", models.PositiveIntegerField(default=0)),
                ("live_questions", models.PositiveIntegerField(default=0)),
                ("display", models.BooleanField(default=False)),
                (
                    "active_participants",
                    models.ManyToManyField(to=settings.AUTH_USER_MODEL),
                ),
                (
                    "project",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="insight",
                        to="a4projects.project",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
