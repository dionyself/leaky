from graphene_django import DjangoObjectType
from graphene import relay, String
from customers.models import TenantUser
from graphql_jwt.utils import jwt_encode, jwt_payload
# from django.contrib.auth import get_user_model


class UserNode(DjangoObjectType):
    token = String()

    def resolve_token(self, info, **kwargs):
        if info.context.user != self:
            return None
        payload = jwt_payload(self)
        return jwt_encode(payload)

    class Meta:
        model = TenantUser  # get_user_model()
        interfaces = (relay.Node, )
        exclude_fields = ["is_deleted"]
        filter_fields = {
            "created_at": ["lte", "gte", "gt", "lt"],
        }
