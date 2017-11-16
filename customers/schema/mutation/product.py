import graphene
from customers.models import Product


class CreateProduct(graphene.Mutation):
    class Arguments:
        code = graphene.Int()
        existence_type = graphene.String()
        asset_type = graphene.String()
        category = graphene.String()
        name = graphene.String()
        properties = graphene.String()

    product_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        try:
            product = Product.objects.create(**args)
            ok = True
        except:
            product = None

        return CreateProduct(
            product_id=product and product.id or 0,
            ok=ok)
