from graphene_django import DjangoObjectType
from graphene import relay
from customers.models import Group


class GroupNode(DjangoObjectType):
    class Meta:
        model = Group
        interfaces = (relay.Node, )
        exclude_fields = ["related_group"]
        filter_fields = {
            "created_at": ["lte", "gte", "gt", "lt"],
        }
