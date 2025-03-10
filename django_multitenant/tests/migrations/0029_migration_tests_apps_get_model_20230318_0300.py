# Generated by Django 4.1.7 on 2023-03-18 08:00

from django.db import migrations

from ..models import MigrationUseInMigrationsModel
from django.apps import apps as apps_global


def test_valid_model(model_class):
    assert model_class.objects.__class__.__name__ == "TenantManager"

    model_class.objects.create(name="test")


def test_invalid_model(apps):
    model_from_apps = apps.get_model("tests", "MigrationUseInMigrationsModel")
    try:
        model_from_apps.objects.create(name="test")
    except AttributeError as e:
        assert str(e) == (
            "apps.get_model method should not be used to get the model MigrationUseInMigrationsModel."
            "Either import the model directly or use the module apps under the module django.apps."
        )


# pylint: disable=unused-argument
def empty_users(apps, schema_editor):
    model_from_global = apps_global.get_model("tests", "MigrationUseInMigrationsModel")
    test_valid_model(model_from_global)

    test_valid_model(MigrationUseInMigrationsModel)

    test_invalid_model(apps)


class Migration(migrations.Migration):
    dependencies = [
        ("tests", "0028_migrationuseinmigrationsmodel_alter_account_managers_and_more"),
    ]

    operations = [
        migrations.RunPython(empty_users),
    ]
