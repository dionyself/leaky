import graphene
from customers.models import ReviewComment


class CreateReviewComment(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int()
        content = graphene.String()
        is_deleted = graphene.Boolean()

    review_comment_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        try:
            review_comment = ReviewComment.objects.create(**args)
            ok = True
        except:
            review_comment = None

        return CreateReviewComment(
            review_comment_id=review_comment and review_comment.id or 0,
            ok=ok)


class UpdateReviewComment(graphene.Mutation):
    class Arguments:
        pk = graphene.Int()
        user_id = graphene.Int()
        content = graphene.String()
        is_deleted = graphene.Boolean()

    review_comment_id = graphene.Int()
    ok = graphene.Boolean()

    def mutate(self, info, **args):

        ok = False
        review_comment = None

        try:
            if 'pk' in args:
                pk = args.pop("pk")
                ReviewComment.objects.filter(id=pk).update(**args)
                review_comment = ReviewComment.objects.filter(id=pk).first()
                ok = True
        except:
            review_comment = None

        return UpdateReviewComment(
            review_comment_id=review_comment and review_comment.id or 0,
            ok=ok)
