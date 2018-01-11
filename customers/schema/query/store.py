from graphene_django import DjangoObjectType
from graphene import relay
from tenant_schemas.utils import get_tenant_model


class StoreNode(DjangoObjectType):
    class Meta:
        model = get_tenant_model()
        interfaces = (relay.Node, )
        exclude_fields = ["is_deleted"]
        filter_fields = {
            "created_at": ["lte", "gte", "gt", "lt"],
        }
