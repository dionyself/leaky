import graphene
from customers.models import Client
from tenant_users.tenants.tasks import provision_tenant


class CreateClient(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        subdomain = graphene.String()
        description = graphene.String()
        group_id = graphene.Int()
        user_email = graphene.Int()
        phone = graphene.String()
        latitude = graphene.Float()
        longitude = graphene.Float()
        time_zone = graphene.String()
        is_active = graphene.Boolean()
        is_deleted = graphene.Boolean()

    client_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        try:
            domain_url = provision_tenant(
                args.pop("name", ""), args.pop("subdomain", ""), args.pop("user_email", ""), is_staff=False)
            tenant = Client.objects.filter(domain_url=domain_url).update(**args)
            ok = True
        except:
            tenant = None

        return CreateClient(
            client_id=tenant and tenant.id or 0,
            ok=ok)


class UpdateClient(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        name = graphene.String()
        description = graphene.String()
        group_id = graphene.Int()
        # user_email = graphene.Int() can't change ower in the mean while
        phone = graphene.String()
        latitude = graphene.Float()
        longitude = graphene.Float()
        time_zone = graphene.String()
        is_active = graphene.Boolean()
        is_deleted = graphene.Boolean()

    client_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        client = None

        try:
            if 'pk' in args:
                pk = args.pop("pk")
                Client.objects.filter(id=pk).update(**args)
                client = Client.objects.filter(id=pk).first()
                ok = True
        except:
            client = None

        return UpdateClient(
            client_id=client and client.id or 0,
            ok=ok)
