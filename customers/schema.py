from graphene import Field, relay, ObjectType
from graphene.types.generic import GenericScalar
from graphene_django.debug import DjangoDebug
from graphene_django.filter import DjangoFilterConnectionField

from django.conf import settings


class Mutation(object):
    #create_product = CreateProduct.Field()
    #update_product = UpdateProduct.Field()
    pass


class Query(ObjectType):

    #Product = relay.Node.Field(ProductNode)
    #Products = DjangoFilterConnectionField(ProductNode)

    debug = Field(DjangoDebug, name='__debug')

    about = GenericScalar()

    def resolve_about(self, args, request, info):
        return {
            "API version": settings.LEAKY_VERSION}
