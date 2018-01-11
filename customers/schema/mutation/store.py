import graphene
from tenant_schemas.utils import get_tenant_model
from tenant_users.tenants.tasks import provision_tenant


class CreateStore(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        subdomain = graphene.String()
        description = graphene.String()
        corporation_id = graphene.Int()
        user_email = graphene.Int()
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
            domain_url = provision_tenant(
                args.pop("name", ""), args.pop("subdomain", ""), args.pop("user_email", ""), is_staff=False)
            store = get_tenant_model().objects.filter(domain_url=domain_url).update(**args)
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
                ok = True
        except:
            store = None

        return UpdateStore(
            store_id=store and store.id or 0,
            ok=ok)
