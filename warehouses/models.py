from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.postgres.fields import JSONField
from customers.models import Product


class Asset(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, help_text="Global product_id.")
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', help_text="The Asset price.")
    existence = models.IntegerField(default=0, help_text="Amount of assets available.")
    properties = JSONField(null=True, blank=True, help_text="Using custom properties for local assets only")
    tags = models.TextField(null=True, blank=True, help_text="custom code.")
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
        unique_together = ('product', 'id',)
