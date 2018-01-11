import graphql_jwt
from graphene import ObjectType
from .product import CreateProduct
from .product import UpdateProduct
from .corporation import CreateCorporation
from .corporation import UpdateCorporation
from .review_comment import CreateReviewComment
from .review_comment import UpdateReviewComment
from .review import CreateReview
from .review import UpdateReview
from .user import CreateUser
from .user import UpdateUser
from .store import CreateStore
from .store import UpdateStore
from .login import LogIn


class Mutation(ObjectType):
    create_product = CreateProduct.Field()
    update_product = UpdateProduct.Field()
    create_corporation = CreateCorporation.Field()
    update_corporation = UpdateCorporation.Field()
    create_review_comment = CreateReviewComment.Field()
    update_review_comment = UpdateReviewComment.Field()
    create_review = CreateReview.Field()
    update_review = UpdateReview.Field()
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    create_store = CreateStore.Field()
    update_store = UpdateStore.Field()
    login = LogIn.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
