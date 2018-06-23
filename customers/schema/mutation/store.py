import graphene
from django_tenants.utils import get_tenant_model
from django.contrib.auth import get_user_model
from tenant_users.tenants.tasks import provision_tenant


class CreateStore(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        subdomain = graphene.String()
        description = graphene.String()
        corporation_id = graphene.Int()
        user_email = graphene.String()
        phone = graphene.String()
        latitude = graphene.Float()
        longitude = graphene.Float()
        time_zone = graphene.String()
        is_active = graphene.Boolean()
        is_deleted = graphene.Boolean()

    store_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        try:
            if args.get("user_email"):
                user = get_user_model().objects.filter(email=args["user_email"]).first()
                assert user, "Invalid user_email"
                assert user.corporation_id == args.get("corporation_id"), "user/corporation missmatch"
            domain_url = provision_tenant(
                args.pop("name", ""), args.pop("subdomain", ""), args.pop("user_email", ""), is_staff=False)
            store = get_tenant_model().objects.filter(domains__domain=domain_url).update(**args)
            ok = True
        except:
            store = None

        return CreateStore(
            store_id=store and store.id or 0,
            ok=ok)


class UpdateStore(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        name = graphene.String()
        description = graphene.String()
        corporation_id = graphene.Int()
        # user_email = graphene.Int() can't change ower in the mean while
        add_users = graphene.List(graphene.Int)
        remove_users = graphene.List(graphene.Int)
        phone = graphene.String()
        latitude = graphene.Float()
        longitude = graphene.Float()
        time_zone = graphene.String()
        is_active = graphene.Boolean()
        is_deleted = graphene.Boolean()

    store_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        store = None

        try:
            if 'pk' in args:
                pk = args.pop("pk")
                get_tenant_model().objects.filter(id=pk).update(**args)
                store = get_tenant_model().objects.filter(id=pk).first()
                if args.get("add_users"):
                    for user_id in args["add_users"]:
                        user = get_user_model().objects.get(pk=user_id)
                        assert user and user.corporation_id == store.corporation_id, "user/corporation missmatch"
                        store.add_user(user, is_staff=False)
                if args.get("remove_users"):
                    for user_id in args["add_users"]:
                        user = get_user_model().objects.get(pk=user_id)
                        assert user and user.corporation_id == store.corporation_id, "user/corporation missmatch"
                        store.remove_user(user)
                ok = True
        except:
            store = None

        return UpdateStore(
            store_id=store and store.id or 0,
            ok=ok)
