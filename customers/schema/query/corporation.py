from graphene_django import DjangoObjectType
from graphene import relay
from customers.models import Corporation


class CorporationNode(DjangoObjectType):
    class Meta:
        model = Corporation
        interfaces = (relay.Node, )
        exclude_fields = ["related_corporation"]
        filter_fields = {
            "created_at": ["lte", "gte", "gt", "lt"],
        }
