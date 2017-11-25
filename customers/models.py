from django.db import models
from django.contrib.postgres.fields import JSONField
from tenant_users.tenants.models import TenantBase
from tenant_users.tenants.models import UserProfile
from django.utils.translation import gettext as _


class TenantUser(UserProfile):
    name = models.CharField(_("Name"), max_length=100, blank=True)


class Group(models.Model):
    name = models.CharField(max_length=100, help_text="Group Name.")
    description = models.CharField(max_length=200, null=True, blank=True)
    properties = JSONField(null=True, blank=True, help_text="The group properties.")
    related_group = models.ForeignKey("self", null=True)
    phone = models.CharField(max_length=100, help_text="Local Phone.")
    is_active = models.BooleanField(default=True)


class Client(TenantBase):
    created_on = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100, help_text="Local Name.")
    description = models.TextField(max_length=200)
    group = models.ForeignKey(Group, null=True, blank=True, help_text="Corporation")
    phone = models.CharField(max_length=100, help_text="Local Phone.")
    latitude = models.FloatField(null=True, blank=True, help_text="coordinates.")
    longitude = models.FloatField(null=True, blank=True, help_text="coodinates.")
    time_zone = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    auto_create_schema = True


class Product(models.Model):
    code = models.IntegerField(help_text="Universal barcode.")
    code_type = models.TextField(help_text="Barcode type.")
    existence_type = models.TextField(help_text="Existence type (Pound, MB, centimeter).")
    name = models.TextField(help_text="Product name.")
    properties = JSONField(null=True, blank=True, help_text="The event properties.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
