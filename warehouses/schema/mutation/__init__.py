from graphene import ObjectType
from .asset import CreateAsset
from .asset import UpdateAsset


class Mutation(ObjectType):
    create_asset = CreateAsset.Field()
    update_asset = UpdateAsset.Field()
