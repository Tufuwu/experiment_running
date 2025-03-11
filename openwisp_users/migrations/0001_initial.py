# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 17:12

import uuid

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import organizations.base
import organizations.fields
from django.conf import settings
from django.db import migrations, models

import openwisp_users.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [('auth', '0008_alter_user_username_max_length')]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                (
                    'last_login',
                    models.DateTimeField(
                        blank=True, null=True, verbose_name='last login'
                    ),
                ),
                (
                    'is_superuser',
                    models.BooleanField(
                        default=False,
                        help_text='Designates that this user has all permissions without explicitly assigning them.',
                        verbose_name='superuser status',
                    ),
                ),
                (
                    'username',
                    models.CharField(
                        error_messages={
                            'unique': 'A user with that username already exists.'
                        },
                        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name='username',
                    ),
                ),
                (
                    'first_name',
                    models.CharField(
                        blank=True, max_length=30, verbose_name='first name'
                    ),
                ),
                (
                    'last_name',
                    models.CharField(
                        blank=True, max_length=30, verbose_name='last name'
                    ),
                ),
                (
                    'email',
                    models.EmailField(
                        blank=True, max_length=254, verbose_name='email address'
                    ),
                ),
                (
                    'is_staff',
                    models.BooleanField(
                        default=False,
                        help_text='Designates whether the user can log into this admin site.',
                        verbose_name='staff status',
                    ),
                ),
                (
                    'is_active',
                    models.BooleanField(
                        default=True,
                        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                        verbose_name='active',
                    ),
                ),
                (
                    'date_joined',
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name='date joined'
                    ),
                ),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ('bio', models.TextField(blank=True, verbose_name='bio')),
                ('url', models.URLField(blank=True, verbose_name='URL')),
                (
                    'company',
                    models.CharField(blank=True, max_length=30, verbose_name='company'),
                ),
                (
                    'location',
                    models.CharField(
                        blank=True, max_length=128, verbose_name='location'
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            managers=[('objects', openwisp_users.base.models.UserManager())],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                (
                    'name',
                    models.CharField(
                        help_text='The name of the organization', max_length=200
                    ),
                ),
                ('is_active', models.BooleanField(default=True)),
                (
                    'created',
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'modified',
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'slug',
                    organizations.fields.SlugField(
                        blank=True,
                        editable=False,
                        help_text='The name in all lowercase, suitable for URL identification',
                        max_length=200,
                        populate_from='name',
                        unique=True,
                    ),
                ),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'description',
                    models.TextField(blank=True, verbose_name='description'),
                ),
                (
                    'email',
                    models.EmailField(blank=True, max_length=254, verbose_name='email'),
                ),
                ('url', models.URLField(blank=True, verbose_name='URL')),
            ],
            options={
                'verbose_name_plural': 'organizations',
                'verbose_name': 'organization',
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OrganizationOwner',
            fields=[
                (
                    'created',
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'modified',
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'organization',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='owner',
                        to='openwisp_users.Organization',
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'organization owners',
                'verbose_name': 'organization owner',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                (
                    'created',
                    organizations.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    'modified',
                    organizations.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                ('is_admin', models.BooleanField(default=False)),
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='organization_users',
                        to='openwisp_users.Organization',
                    ),
                ),
                (
                    'user',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='openwisp_users_organizationuser',
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'organization users',
                'verbose_name': 'organization user',
                'abstract': False,
                'ordering': ['organization', 'user'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[],
            options={
                'verbose_name_plural': 'groups',
                'verbose_name': 'group',
                'proxy': True,
            },
            bases=('auth.group',),
            managers=[('objects', django.contrib.auth.models.GroupManager())],
        ),
        migrations.AddField(
            model_name='organizationowner',
            name='organization_user',
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to='openwisp_users.OrganizationUser',
            ),
        ),
        migrations.AddField(
            model_name='organization',
            name='users',
            field=models.ManyToManyField(
                related_name='openwisp_users_organization',
                through='openwisp_users.OrganizationUser',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(
                blank=True,
                help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                related_name='user_set',
                related_query_name='user',
                to='auth.Group',
                verbose_name='groups',
            ),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(
                blank=True,
                help_text='Specific permissions for this user.',
                related_name='user_set',
                related_query_name='user',
                to='auth.Permission',
                verbose_name='user permissions',
            ),
        ),
        migrations.AlterUniqueTogether(
            name='organizationuser', unique_together=set([('user', 'organization')])
        ),
    ]
