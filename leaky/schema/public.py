import graphene
import customers.schema


class Query(
    customers.schema.Query
):
    pass


class Mutation(
    customers.schema.Mutation
):
    pass


public_schema = graphene.Schema(query=Query, mutation=Mutation)
