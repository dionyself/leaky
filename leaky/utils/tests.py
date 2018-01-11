import unittest
from traceback import print_exc
from django.conf import settings
from tenant_users.tenants.utils import create_public_tenant
from tenant_users.tenants.tasks import provision_tenant
from customers.models import StoreUser
from graphene.test import Client as GqlClient
from tenant_schemas.utils import schema_context
from leaky.schema import public_schema, tenant_schema
from customers.models import Store

main_host = settings.TENANT_USERS_DOMAIN
main_email = settings.SYSTEM_EMAIL
test_tenant_name = settings.TEST_TENANT_NAME
test_tenant_host = settings.TEST_TENANT_HOST
test_tenant_email = settings.ADMIN_EMAIL
test_tenant_password = settings.ADMIN_PASSWORD
gql_public_client = GqlClient(public_schema)
gql_tenant_client = GqlClient(tenant_schema)


def execute_gql_query(query, tenant_name="public", tenant=None, as_user=None):
    if not tenant:
        with schema_context("public"):
            if tenant_name == "public":
                tenant = Store.objects.filter(
                    domain_url=settings.TENANT_USERS_DOMAIN).first()
                with schema_context(tenant.schema_name):
                    return gql_public_client.execute(query).get("data")
            elif tenant_name == "test":
                tenant = Store.objects.filter(
                    domain_url="%s.%s" % (settings.TEST_TENANT_HOST, settings.TENANT_USERS_DOMAIN)).first()
            else:
                tenant = Store.objects.filter(
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

    @classmethod
    def setUpClass(cls):
        # Create public tenant, test tenant and user.
        try:
            create_public_tenant(main_host, main_email)
            user = StoreUser.objects.create_user(email=test_tenant_email, password=test_tenant_password, is_active=True)
            fqdn = provision_tenant(test_tenant_name, test_tenant_host, test_tenant_email)
        except Exception as e:
            print_exc()

    def execute(self, *args, **kwargs):
        return execute_gql_query(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass
