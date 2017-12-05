from graphene_django import DjangoObjectType
from graphene import relay
from warehouses.models import Invoice


class InvoiceNode(DjangoObjectType):
    class Meta:
        model = Invoice
        interfaces = (relay.Node, )
        exclude_fields = ["is_deleted"]
        #only_fields = ["created_at"]
        filter_fields = {
            "created_at": ["lte", "gte", "gt", "lt"],
        }
