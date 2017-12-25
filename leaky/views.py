from graphene_django.views import GraphQLView
from django.contrib.auth.mixins import LoginRequiredMixin


class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    def execute(self, *args, **kwargs):
        #from graphql.execution.middleware import MiddlewareManager
        #kwargs["middleware"] = MiddlewareManager(*kwargs["middleware"], wrap_in_promise=False)
        return super().execute(*args, allow_subscriptions=True, **kwargs)
