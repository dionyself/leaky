from graphene import ObjectType
from .asset import CreateAsset


class Mutation(ObjectType):
    create_asset = CreateAsset.Field()
    # update_asset = UpdateAsset.Field()
    pass
