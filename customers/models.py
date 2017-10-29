from django.db import models
from tenant_schemas.models import TenantMixin


class Client(TenantMixin):
    created_on = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=100, unique=True)
    time_zone = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    auto_create_schema = True
