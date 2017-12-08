import graphene
from customers.models import Product
from graphene.types.generic import GenericScalar


class CreateProduct(graphene.Mutation):
    class Arguments:
        code = graphene.Int()
        existence_type = graphene.String()
        asset_type = graphene.String()
        category = graphene.String()
        name = graphene.String()
        properties = GenericScalar()

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


class UpdateProduct(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        code = graphene.Int()
        existence_type = graphene.String()
        asset_type = graphene.String()
        category = graphene.String()
        name = graphene.String()
        properties = GenericScalar()

    product_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        product = None

        try:
            if 'pk' in args:
                pk = args.pop("pk")
                Product.objects.filter(id=pk).update(**args)
                product = Product.objects.filter(id=pk).first()
                ok = True
        except:
            product = None

        return UpdateProduct(
            product_id=product and product.id or 0,
            ok=ok)
