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
            user_id = args.pop("user_id", 0)
            if args.get("related_corporation_id") == 0:
                del args["related_corporation_id"]
            if user_id > 0:
                user = get_user_model().objects.filter(pk=user_id).first()
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
        id = graphene.Int()
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
        corporation = None

        try:
            if 'id' in args:
                id = args.pop("id")
                Corporation.objects.filter(id=id).update(**args)
                corporation = Corporation.objects.filter(id=id).first()
                ok = True
        except:
            corporation = None

        return UpdateCorporation(
            corporation_id=corporation and corporation.id or 0,
            ok=ok)
