from graphene import ObjectType
from .asset import CreateAsset
from .asset import UpdateAsset
from .asset_tag import CreateAssetTag
from .asset_tag import UpdateAssetTag


class Mutation(ObjectType):
    create_asset = CreateAsset.Field()
    update_asset = UpdateAsset.Field()
    create_asset_tag = CreateAssetTag.Field()
    update_asset_tag = UpdateAssetTag.Field()
