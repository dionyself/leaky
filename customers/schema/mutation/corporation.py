import graphene
from customers.models import Corporation
from django.contrib.auth import get_user_model
from graphene.types.generic import GenericScalar


class CreateCorporation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        properties = GenericScalar()
        related_corporation_id = graphene.Int()
        user_id = graphene.Int()
        phone = graphene.String()
        is_active = graphene.Boolean()
        is_deleted = graphene.Boolean()

    corporation_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        try:
            user = None
            if args.get("user_id"):
                user = get_user_model().objects.filter(pk=args.pop("user_id")).first()
                assert user, "Error: invalid value for user_id"
            corporation = Corporation.objects.create(**args)
            if user and corporation:
                user.update(corporation_id=corporation.id)
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
