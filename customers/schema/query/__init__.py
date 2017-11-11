from graphene import Field, ObjectType
from graphene.types.generic import GenericScalar
from graphene_django.debug import DjangoDebug
from django.conf import settings
# from .product import ProductNode


class Query(ObjectType):

    debug = Field(DjangoDebug, name='__debug')

    about = GenericScalar()

    def resolve_about(self, args, request, info):
        return {
            "API version": settings.LEAKY_VERSION}
