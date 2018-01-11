import graphene
from customers.models import Corporation
from graphene.types.generic import GenericScalar


class CreateCorporation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        properties = GenericScalar()
        related_corporation_id = graphene.Int()
        phone = graphene.String()
        is_active = graphene.Boolean()
        is_deleted = graphene.Boolean()

    corporation_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        try:
            corporation = Corporation.objects.create(**args)
            ok = True
        except:
            corporation = None

        return CreateCorporation(
            corporation_id=corporation and corporation.id or 0,
            ok=ok)


class UpdateCorporation(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        name = graphene.String()
        description = graphene.String()
        properties = graphene.String()
        related_group_id = graphene.Int()
        phone = graphene.String()
        is_active = graphene.Boolean()
        is_deleted = graphene.Boolean()

    corporation_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        corporation = None

        try:
            if 'pk' in args:
                pk = args.pop("pk")
                Corporation.objects.filter(id=pk).update(**args)
                corporation = Corporation.objects.filter(id=pk).first()
                ok = True
        except:
            corporation = None

        return UpdateCorporation(
            corporation_id=corporation and corporation.id or 0,
            ok=ok)
