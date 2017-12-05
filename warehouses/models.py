from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.postgres.fields import JSONField
from customers.models import Product


class Asset(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, help_text="Global product_id.")
    modded_product_name = models.TextField(null=True, blank=True, unique=True, help_text="Name for custominzed/variant product")
    cost = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', help_text="The Asset raw cost.")
    minimal_earnings = models.IntegerField(default=0, help_text="Minimal earning expected.")
    availability = models.IntegerField(default=0, help_text="Amount of assets available.")
    existence = models.IntegerField(default=0, help_text="Amount of assets present in warehose.")
    properties = JSONField(null=True, blank=True, help_text="Using custom properties for local assets only")
    asset_type = models.TextField(default="product", help_text="Asset type: product/service/subscription/warranty")
    category = models.TextField(null=True, blank=True, help_text="Department/location of the product")
    starts_at = models.DateTimeField(auto_now_add=True,
        help_text="start date of an offer/product: (start_at = now by default")
    expires_at = models.DateTimeField(null=True, blank=True,
        help_text="Expiration date of an offer/product: (exprires_at = created_at + duration)")
    duration = models.DurationField(null=True, blank=True, help_text="Duration of a given offer/product (auto calculated)")
    is_deleted = models.BooleanField(default=False, help_text="Assets cannot be deleted, just mark it as deleted")
    is_expired = models.BooleanField(default=False, help_text="Force the Asset to expire")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["id"]


class AssetTag(models.Model):
    name = models.TextField(unique=True, help_text="Tag name")
    description = models.TextField(null=True, blank=True, help_text="Description")
    tag_type = models.TextField(null=True, blank=True, help_text="tag_type: earnings, taxes, discounts")
    priority = models.IntegerField(default=0, help_text="tag priority.")
    properties = JSONField(null=True, blank=True, help_text="Properties")
    assets = models.ManyToManyField(Asset, help_text="tagged assets.")
    is_deleted = models.BooleanField(default=False, help_text="Tags cannot be deleted, just mark it as deleted")
    is_disabled = models.BooleanField(default=False, help_text="Disabled")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Invoice(models.Model):
    fiscal_id = models.TextField(help_text="Tag name")
    header = JSONField(null=True, blank=True, help_text="header data")
    body = JSONField(null=True, blank=True, help_text="Item list")
    footer = JSONField(null=True, blank=True, help_text="footer data")
    is_reversed = models.BooleanField(default=False, help_text="Tags cannot be deleted, just mark it as deleted")
    is_blocked = models.BooleanField(default=True, help_text="invoice processed")
    is_processed = models.BooleanField(default=False, help_text="invoice processed")
    created_at = models.DateTimeField(auto_now_add=True)
