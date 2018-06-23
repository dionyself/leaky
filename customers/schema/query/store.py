import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from django_tenants.utils import get_tenant_model


class StoreNode(DjangoObjectType):

    domains = graphene.List(graphene.String)

    def resolve_domains(self, info, **kwargs):
        domains = self.domains.all()
        domain_strings = []
        for domain in domains:
            domain_strings.append(domain.domain)
        return domain_strings

    class Meta:
        model = get_tenant_model()
        interfaces = (relay.Node, )
        exclude_fields = ["is_deleted"]
        filter_fields = {
            "created_at": ["lte", "gte", "gt", "lt"],
        }
