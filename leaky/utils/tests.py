import unittest
from django.conf import settings
from graphene.test import Client as GqlClient
from tenant_schemas.utils import schema_context
from leaky.schema import public_schema, tenant_schema
from customers.models import Client

gql_public_client = GqlClient(public_schema)
gql_tenant_client = GqlClient(tenant_schema)


def execute_gql_query(query, tenant_name="public", tenant=None, as_user=None):
    if not tenant:
        with schema_context("public"):
            if tenant_name == "public":
                tenant = Client.objects.filter(
                    domain_url=settings.TENANT_USERS_DOMAIN).first()
                with schema_context(tenant.schema_name):
                    return gql_public_client.execute(query).get("data")
            elif tenant_name == "test":
                tenant = Client.objects.filter(
                    domain_url="%s.%s" % (settings.TEST_TENANT_HOST, settings.TENANT_USERS_DOMAIN)).first()
            else:
                tenant = Client.objects.filter(
                    domain_url="%s.%s" % (tenant_name, settings.TENANT_USERS_DOMAIN)).first()
    with schema_context(tenant.schema_name):
        return gql_tenant_client.execute(query).get("data")


class BaseTestCase(unittest.TestCase):
    PUBLIC_TENANT = {
        "user": "test",
        "tenant": "tennat",
        "schema_name": "schema_name"
        }
    TENANTS = {
        "test": {
            "user": "test",
            "tennat": "test",
            "schema_name": "schema_name"
        }
    }

    execute_gql_query = execute_gql_query
    pass
