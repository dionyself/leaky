from graphene import ObjectType
from .product import CreateProduct
from .product import UpdateProduct
from .group import CreateGroup
from .group import UpdateGroup
from .review_comment import CreateReviewComment
from .review_comment import UpdateReviewComment
from .review import CreateReview
from .review import UpdateReview
from .user import CreateUser
from .user import UpdateUser
from .tenant import CreateClient
from .tenant import UpdateClient


class Mutation(ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    create_group = CreateGroup.Field()
    update_group = UpdateGroup.Field()
    create_review_comment = CreateReviewComment.Field()
    update_review_comment = UpdateReviewComment.Field()
    create_review = CreateReview.Field()
    update_review = UpdateReview.Field()
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    create_store = CreateClient.Field()
    update_store = UpdateClient.Field()
