from django.db import models
from djmoney.models.fields import MoneyField
from django.contrib.postgres.fields import JSONField


class Asset(models.Model):
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD', help_text="The Asset price.")
    existence = models.IntegerField(default=0, help_text="Amount of assets available.")
    properties = JSONField(null=True, blank=True, help_text="Using custom properties for local assets only")
    code = models.TextField(default="", help_text="custom_code.")
    product_id = models.IntegerField(null=True, help_text="Global product_id.")
    asset_type = models.TextField(default="product", help_text="Asset type: product/service/subscription/warranty")
    category = models.TextField(null=True, blank=True, help_text="Department/location of the product")
    duration = models.DurationField(null=True, blank=True, help_text="Duration of a given offer")
    expires_at = models.DateTimeField(null=True, blank=True,
        help_text="Expiration date of an offer/product: (exprires_at = created_at + duration)")
    is_deleted = models.BooleanField(default=False, help_text="Assets cannot be deleted, just mark it as deleted")
    is_expired = models.BooleanField(default=False, help_text="Force the Asset to expire")

    class Meta:
        ordering = ["id"]
