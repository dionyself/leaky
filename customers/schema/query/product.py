from graphene_django import DjangoObjectType
from graphene import relay
from customers.models import Product


class ProductNode(DjangoObjectType):
    class Meta:
        model = Product
        interfaces = (relay.Node, )
        exclude_fields = ["is_deleted"]
        filter_fields = {
            "created_at": ["lte", "gte", "gt", "lt"],
        }
