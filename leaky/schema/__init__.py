import graphene
import customers.schema
import warehouses.schema


class Query(
    customers.schema.Query
):
    pass


class Mutation(
    customers.schema.Mutation
):
    pass


class TenantSubscription(
    # Subscription, # no subscription on public_schema
    warehouses.schema.Subscription,
):
    pass


class TenantQuery(
    Query,
    warehouses.schema.Query,
):
    pass


class TenantMutation(
    Mutation,
    warehouses.schema.Mutation,
):
    pass


public_schema = graphene.Schema(query=Query, mutation=Mutation)
tenant_schema = graphene.Schema(query=TenantQuery, mutation=TenantMutation)  # subscription=TenantSubscription)
