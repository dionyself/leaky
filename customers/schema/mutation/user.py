import graphene
from django.contrib.auth import get_user_model
from graphene.types.generic import GenericScalar


class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        email = graphene.String()
        password = graphene.String()
        corporation_id = graphene.Int()
        properties = GenericScalar()
        is_active = graphene.Boolean()
        is_superuser = graphene.Boolean()
        is_staff = graphene.Boolean()
        is_deleted = graphene.Boolean()

    user_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        try:
            user = get_user_model().objects.create_user(
                email=args.pop("email", ""),
                password=args.pop("password", ""),
                is_active=args.pop("is_active", False))
            user.update(**args)
            user.save()
            ok = True
        except:
            user = None

        return CreateUser(
            user_id=user and user.id or 0,
            ok=ok)


class UpdateUser(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        name = graphene.String()
        corporation_id = graphene.Int()
        properties = GenericScalar()
        is_active = graphene.Boolean()
        is_deleted = graphene.Boolean()

    user_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        user = None

        try:
            if 'pk' in args:
                pk = args.pop("pk")
                user = get_user_model().objects.filter(id=pk).first()
                ok = True
        except:
            user = None

        return UpdateUser(
            user_id=user and user.id or 0,
            ok=ok)
