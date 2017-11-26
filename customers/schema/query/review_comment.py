from graphene_django import DjangoObjectType
from graphene import relay
from customers.models import ReviewComment


class ReviewCommentNode(DjangoObjectType):
    class Meta:
        model = ReviewComment
        interfaces = (relay.Node, )
        exclude_fields = ["is_deleted"]
        filter_fields = {
            "created_at": ["lte", "gte", "gt", "lt"],
        }
