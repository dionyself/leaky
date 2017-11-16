youimport graphene
import customers.schema
import warehouses.schema


class Query(
    warehouses.schema.Query,
    customers.schema.Query
):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(
    warehouses.schema.Mutation,
    customers.schema.Mutation
):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
