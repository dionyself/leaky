from graphene import ObjectType
from .product import CreateProduct


class Mutation(ObjectType):
    create_product = CreateProduct.Field()
    # update_product = UpdateProduct.Field()
