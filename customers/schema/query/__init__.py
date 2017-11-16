from graphene import Field, relay, ObjectType
from graphene.types.generic import GenericScalar
from graphene_django.debug import DjangoDebug
from graphene_django.filter import DjangoFilterConnectionField
from django.conf import settings
from .product import ProductNode


class Query(ObjectType):

    product = relay.Node.Field(ProductNode)
    products = DjangoFilterConnectionField(ProductNode)
    debug = Field(DjangoDebug, name='__debug')

    about = GenericScalar()

    def resolve_about(self, args, request, info):
        return {
            "API version": settings.LEAKY_VERSION}
