#!/usr/bin/env python
import os
from traceback import print_exc
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leaky.settings")
django.setup()

from django.conf import settings
from tenant_users.tenants.utils import create_public_tenant
from tenant_users.tenants.tasks import provision_tenant
from customers.models import TenantUser

main_host = settings.TENANT_USERS_DOMAIN
main_email = settings.SYSTEM_EMAIL

test_tenant_name = settings.TEST_TENANT_NAME
test_tenant_host = settings.TEST_TENANT_HOST
test_tenant_email = settings.ADMIN_EMAIL
test_tenant_password = settings.ADMIN_PASSWORD

# Create public tenant and user.
create_public_tenant(main_host, main_email)
user = TenantUser.objects.create_user(email=test_tenant_email, password=test_tenant_password, is_active=True)

print("Creating a test client Using subdomain [{}], name [{}]... to avoid this set AUTO_CREATE_TEST_TENANT to False".format(
    test_tenant_host, test_tenant_name))

try:
    if settings.AUTO_CREATE_TEST_TENANT:
        print("Creating a test client Using host [{}] and name [{}]... to avoid this set AUTO_CREATE_TEST_TENANT to False".format(test_tenant_host, test_tenant_name))
        # create tenant
        fqdn = provision_tenant(test_tenant_name, test_tenant_host, test_tenant_email)
        print("Added Client: {}".format(test_tenant_name))
except Exception as e:
    print_exc()
    print(e)
    print("Unable to configure test schema.")
