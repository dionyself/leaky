import graphene
from customers.models import Group
from graphene.types.generic import GenericScalar


class CreateGroup(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        description = graphene.String()
        properties = GenericScalar()
        related_group_id = graphene.Int()
        phone = graphene.String()
        is_active = graphene.Boolean()
        is_deleted = graphene.Boolean()

    group_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        try:
            group = Group.objects.create(**args)
            ok = True
        except:
            group = None

        return CreateGroup(
            group_id=group and group.id or 0,
            ok=ok)


class UpdateGroup(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        name = graphene.String()
        description = graphene.String()
        properties = graphene.String()
        related_group_id = graphene.Int()
        phone = graphene.String()
        is_active = graphene.Boolean()
        is_deleted = graphene.Boolean()

    group_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        group = None

        try:
            if 'pk' in args:
                pk = args.pop("pk")
                Group.objects.filter(id=pk).update(**args)
                group = Group.objects.filter(id=pk).first()
                ok = True
        except:
            group = None

        return UpdateGroup(
            group_id=group and group.id or 0,
            ok=ok)
