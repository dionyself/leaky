from django.db import models
from django.contrib.postgres.fields import JSONField
from tenant_users.tenants.models import TenantBase
from tenant_users.tenants.models import UserProfile
from django.utils.translation import gettext as _


class Corporation(models.Model):
    name = models.CharField(max_length=100, help_text="Group Name.")
    description = models.CharField(max_length=200, null=True, blank=True)
    properties = JSONField(null=True, blank=True, help_text="The group properties.")
    related_corporation = models.ForeignKey("self", null=True)  # probably not needed
    phone = models.CharField(max_length=100, help_text="Local Phone.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


class StoreUser(UserProfile):
    name = models.CharField(_("Name"), max_length=100, blank=True)
    corporation = models.ForeignKey(Corporation, null=True, blank=True, help_text="Corporation")
    properties = JSONField(null=True, blank=True, help_text="The group properties.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)


class Store(TenantBase):
    created_on = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100, help_text="Local Name.")
    description = models.TextField(max_length=200)
    corporation = models.ForeignKey(Corporation, null=True, blank=True, help_text="Corporation")
    phone = models.CharField(max_length=100, help_text="Local Phone.")
    latitude = models.FloatField(null=True, blank=True, help_text="coordinates.")
    longitude = models.FloatField(null=True, blank=True, help_text="coodinates.")
    time_zone = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auto_create_schema = True


class Product(models.Model):
    code = models.IntegerField(null=True, blank=True, help_text="Universal barcode.")
    code_type = models.TextField(help_text="Barcode type.")
    existence_type = models.TextField(help_text="Existence type (Pound, MB, centimeter).")
    name = models.TextField(unique=True, help_text="Product name.")
    properties = JSONField(null=True, blank=True, help_text="The Review properties.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        unique_together = ("code", "code_type")


class Review(models.Model):
    user = models.ForeignKey(StoreUser, help_text="User/Reviewer")
    product = models.ForeignKey(Product, help_text="Product")
    title = models.TextField(help_text="Review Title.")
    content = models.TextField(help_text="Review content.")
    comments = models.TextField(help_text="Review coments.")
    stars = models.IntegerField(help_text="stars.")
    properties = JSONField(null=True, blank=True, help_text="The Review properties.")
    likes = models.ManyToManyField(StoreUser, related_name="reviews_liked", help_text="Likes.")
    dislikes = models.ManyToManyField(StoreUser, related_name="reviews_disliked", help_text="Dislikes.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)


class ReviewComment(models.Model):
    user = models.ForeignKey(StoreUser, help_text="User/Reviewer")
    content = models.TextField(help_text="Comment content.")
    likes = models.ManyToManyField(StoreUser, related_name="review_comments_liked", help_text="Likes.")
    dislikes = models.ManyToManyField(StoreUser, related_name="review_comments_disliked", help_text="Dislikes.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
