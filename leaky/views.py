from graphene_django.views import GraphQLView
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django_subscriptions import depromise_subscription


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    def execute(self, *args, **kwargs):
        #from graphql.execution.middleware import MiddlewareManager
        #kwargs["middleware"] = MiddlewareManager(*kwargs["middleware"], wrap_in_promise=False)
        kwargs["middleware"].append(depromise_subscription)
        return super().execute(*args, allow_subscriptions=True, **kwargs)
