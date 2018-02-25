from graphene_django import DjangoObjectType
from graphene.types.generic import GenericScalar
from graphene import relay
from customers.models import Corporation


class CorporationNode(DjangoObjectType):

    properties = GenericScalar()

    class Meta:
        model = Corporation
        interfaces = (relay.Node, )
        exclude_fields = ["related_corporation"]
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "description": ["exact", "icontains", "istartswith"],
            "phone": ["exact", "icontains", "istartswith"],
            "created_at": ["lte", "gte", "gt", "lt"],
            "updated_at": ["lte", "gte", "gt", "lt"],
            "is_active": ["exact"],
            "is_deleted": ["exact"],
        }
