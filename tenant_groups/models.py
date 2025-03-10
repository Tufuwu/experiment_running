# Copyright (c) 2022-2023 Alexander Todorov <atodorov@otb.bg>
#
# Licensed under GNU Affero General Public License v3 or later (AGPLv3+)
# https://www.gnu.org/licenses/agpl-3.0.html

from django.db import models
from django.conf import settings
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    """
    Per-tenant group definition! See
    https://github.com/kiwitcms/tenants/issues/104#issuecomment-949956789

    Note: essentially copy-pasted from django.contrib.auth b/c we need separate
    records inside tenant's schema.
    """

    relevant_apps = [
        "attachments",
        "bugs",
        "django_comments",
        "linkreference",
        "management",
        "testcases",
        "testplans",
        "testruns",
        "tenant_groups",
        "trackers_integration",
    ]

    name = models.CharField(_("name"), max_length=150, unique=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_("permissions"),
        blank=True,
        related_name="tenant_groups",
    )

    user_set = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="tenant_groups"
    )

    class Meta:
        verbose_name = _("group")
        verbose_name_plural = _("groups")

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)
