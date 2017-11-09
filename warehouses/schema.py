import graphene
from graphene import Field, relay, ObjectType
from graphene.types.generic import GenericScalar
from graphene_django.debug import DjangoDebug
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from warehouses.models import Asset

from django.conf import settings


class AssetNode(DjangoObjectType):
    class Meta:
        model = Asset
        interfaces = (relay.Node, )
        filter_fields = {
            "code": ["exact", "icontains", "istartswith"],
        }


class CreateAsset(graphene.Mutation):
    class Arguments:
        code = graphene.String()

    code = graphene.String()
    ok = graphene.Boolean()

    def mutate(self, info, **args):
        from datetime import datetime

        ok = False
        try:
            asset = Asset.objects.get(code=args['code'])
        except:
            asset = Asset.objects.create(
                code=args['code'], expires_at=datetime.now(), duration=datetime.utcnow()-datetime(1970, 1, 1))
            ok = True

        return CreateAsset(
            code=args.get('code', ""),
            ok=ok)


class Mutation(ObjectType):
    create_asset = CreateAsset.Field()
    #update_asset = UpdateAsset.Field()
    pass


class Query(ObjectType):

    asset = relay.Node.Field(AssetNode)
    assets = DjangoFilterConnectionField(AssetNode)

    debug = Field(DjangoDebug, name='__debug')

    about = GenericScalar()

    def resolve_about(self, info, **args):
        return {
            "API version": settings.LEAKY_VERSION}
