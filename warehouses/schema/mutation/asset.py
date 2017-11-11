import graphene
from datetime import datetime
from warehouses.models import Asset


class CreateAsset(graphene.Mutation):
    class Arguments:
        code = graphene.String()

    code = graphene.String()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        try:
            Asset.objects.get(code=args['code'])
        except:
            Asset.objects.create(
                code=args['code'],
                expires_at=datetime.now(),
                duration=datetime.utcnow()-datetime(1970, 1, 1))
            ok = True

        return CreateAsset(
            code=args.get('code', ""),
            ok=ok)
