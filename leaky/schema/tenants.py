import graphene
from leaky.schema import public
import warehouses.schema


class TenantSubscription(
    warehouses.schema.Subscription,
):
    pass


class TenantQuery(
    public.Query,
    warehouses.schema.Query,
):
    pass


class TenantMutation(
    public.Mutation,
    warehouses.schema.Mutation,
):
    pass


tenant_schema = graphene.Schema(query=TenantQuery, mutation=TenantMutation, subscription=TenantSubscription)
