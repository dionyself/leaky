from graphene_django import DjangoObjectType
from graphene import relay
from warehouses.models import Asset


class AssetNode(DjangoObjectType):
    class Meta:
        model = Asset
        interfaces = (relay.Node, )
        filter_fields = {
            "code": ["exact", "icontains", "istartswith"],
        }
