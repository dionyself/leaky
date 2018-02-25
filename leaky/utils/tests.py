import unittest
from traceback import print_exc
from django.conf import settings
from tenant_users.tenants.utils import create_public_tenant
from tenant_users.tenants.tasks import provision_tenant
from django.contrib.auth import get_user_model
from graphene.test import Client as GqlClient
from tenant_schemas.utils import (get_public_schema_name, get_tenant_model,
                                  schema_context)
from leaky.schema import public_schema, tenant_schema
from customers.models import Corporation

User = get_user_model()
Tenant = get_tenant_model()
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
                tenant = Tenant.objects.filter(
                    domain_url=settings.TENANT_USERS_DOMAIN).first()
                with schema_context(tenant.schema_name):
                    return gql_public_client.execute(query).get("data")
            elif tenant_name == "test":
                tenant = Tenant.objects.filter(
                    domain_url="%s.%s" % (settings.TEST_TENANT_HOST, settings.TENANT_USERS_DOMAIN)).first()
            else:
                tenant = Tenant.objects.filter(
                    domain_url="%s.%s" % (tenant_name, settings.TENANT_USERS_DOMAIN)).first()
    with schema_context(tenant.schema_name):
        return gql_tenant_client.execute(query).get("data")


class BaseTestCase(unittest.TestCase):
    PUBLIC_TENANT = {
        "user": "test",
        "tenant": "tenant",
        "schema_name": "schema_name"
        }
    TENANTS = {
        "test": {
            "user": "user_instance",
            "tenant": "tenant_instance",
            "schema_name": "schema_name"
        }
    }
    TENANT_GROUPS = {
        "test_corporation": {
            "tenant_group": "tenant_group_instance"
        }
    }

    @classmethod
    def setUpClass(cls):
        # Create public tenant, test tenant and user.
        try:
            create_public_tenant(main_host, main_email)
            user = User.objects.create_user(email=test_tenant_email, password=test_tenant_password, is_active=True)
            provision_tenant(test_tenant_name, test_tenant_host, test_tenant_email)
            cls.PUBLIC_TENANT["schema_name"] = get_public_schema_name()
            cls.PUBLIC_TENANT["tenant"] = Tenant.objects.filter(domain_url=settings.TENANT_USERS_DOMAIN).first()
            cls.PUBLIC_TENANT["user"] = User.objects.filter(store__domain_url=settings.TENANT_USERS_DOMAIN).first()
            cls.TENANT_GROUPS["test_corporation"]["tenant_group"] = Corporation.objects.create(name="test_corporation", phone="1-555-5555")
            cls.TENANTS["test"]["user"] = user
            cls.TENANTS["test"]["tenant"] = Tenant.objects.filter(domain_url="%s.%s" % (settings.TEST_TENANT_HOST, settings.TENANT_USERS_DOMAIN)).first()
            cls.TENANTS["test"]["schema_name"] = cls.TENANTS["test"]["tenant"].schema_name
        except Exception as e:
            print_exc()

    @classmethod
    def tearDownClass(cls):
        pass

    def execute(self, *args, **kwargs):
        return execute_gql_query(*args, **kwargs)

    def setUp(self):
        pass

    def tearDown(self):
        pass
