#from djmoney.models.fields import MoneyField
from django.db import models

# Create your models here.


class Asset(models.Model):
    price = models.IntegerField(default=5, help_text="The Asset price.")
    #price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    existence = models.IntegerField(default=5, help_text="The Asset price.")
    # properties = JSONField(null=True, blank=True, help_text="The event properties.")
    code = models.TextField(help_text="custom_code.")
    product_id = models.IntegerField(default=5, help_text="The Asset price.")
    type = models.TextField(help_text="The assetType name.")
    expires_at = models.DateTimeField()
    duration = models.DurationField()

    class Meta:
        ordering = ["id"]
