import graphene
from customers.models import Review
from graphene.types.generic import GenericScalar


class CreateReview(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int()
        product_id = graphene.Int()
        title = graphene.String()
        content = graphene.String()
        comments = graphene.String()
        stars = graphene.Int()
        properties = GenericScalar()
        is_deleted = graphene.Int()

    review_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        try:
            review = Review.objects.create(**args)
            ok = True
        except:
            review = None

        return CreateReview(
            review_id=review and review.id or 0,
            ok=ok)


class UpdateReview(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        product_id = graphene.Int()
        title = graphene.String()
        content = graphene.String()
        comments = graphene.String()
        stars = graphene.Int()
        properties = GenericScalar()
        is_deleted = graphene.Int()

    review_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        review = None

        try:
            if 'pk' in args:
                pk = args.pop("pk")
                Review.objects.filter(id=pk).update(**args)
                review = Review.objects.filter(id=pk).first()
                ok = True
        except:
            review = None

        return UpdateReview(
            review_id=review and review.id or 0,
            ok=ok)
