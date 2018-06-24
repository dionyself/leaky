from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django_subscriptions import depromise_subscription
from graphene_django_extras.views import ExtraGraphQLView
from .permissions import PermissionsMiddleware


class PrivateGraphQLView(LoginRequiredMixin, ExtraGraphQLView):
    def execute(self, *args, **kwargs):
        kwargs["middleware"].append(PermissionsMiddleware())
        kwargs["middleware"].append(depromise_subscription)
        return super().execute(*args, allow_subscriptions=True, **kwargs)
