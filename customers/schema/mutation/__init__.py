from graphene import ObjectType
from .product import CreateProduct
from .product import UpdateProduct


class Mutation(ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
