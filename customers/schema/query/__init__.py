from graphene import Field, relay, ObjectType
from graphene.types.generic import GenericScalar
from graphene_django.debug import DjangoDebug
from graphene_django.filter import DjangoFilterConnectionField
from django.conf import settings
from .product import ProductNode
from .corporation import CorporationNode
from .review_comment import ReviewCommentNode
from .review import ReviewNode
from .store import StoreNode
from .user import UserNode


class Query(ObjectType):

    product = relay.Node.Field(ProductNode)
    products = DjangoFilterConnectionField(ProductNode)
    corporation = relay.Node.Field(CorporationNode)
    corporations = DjangoFilterConnectionField(CorporationNode)
    review_comment = relay.Node.Field(ReviewCommentNode)
    review_comments = DjangoFilterConnectionField(ReviewCommentNode)
    review = relay.Node.Field(ReviewNode)
    reviews = DjangoFilterConnectionField(ReviewNode)
    store = relay.Node.Field(StoreNode)
    stores = DjangoFilterConnectionField(StoreNode)
    user = relay.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode)

    debug = Field(DjangoDebug, name='__debug')

    about = GenericScalar()

    def resolve_about(self, args, request, info):
        return {
            "API version": settings.LEAKY_VERSION}
