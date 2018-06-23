#!/usr/bin/env python
import os
from traceback import print_exc
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leaky.settings")
django.setup()

from django.conf import settings
from tenant_users.tenants.utils import create_public_tenant
from tenant_users.tenants.tasks import provision_tenant
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from customers.models import Corporation, Store


UserModel = get_user_model()
main_host = settings.TENANT_USERS_DOMAIN
main_email = settings.SYSTEM_EMAIL

test_tenant_group_name = settings.TEST_TENANT_GROUP_NAME
test_tenant_name = settings.TEST_TENANT_NAME
test_tenant_host = settings.TEST_TENANT_HOST
test_tenant_email = settings.ADMIN_EMAIL
test_tenant_password = settings.ADMIN_PASSWORD

# Create public tenant and user.
create_public_tenant(main_host, main_email)

# creating permissions
for model in apps.get_models():
    content_type = ContentType.objects.get_for_model(model)
    permission = Permission.objects.create(
        codename='can_read',
        name='Can read %s' % model._meta.verbose_name,
        content_type=content_type)

# creating permissions_group
customer_group = Group.objects.create(name="customer")
seller_group = Group.objects.create(name="seller")
majorseller_group = Group.objects.create(name="majorseller")
purchasingmanager_group = Group.objects.create(name="purchasingmanager")
storeadmin_group = Group.objects.create(name="storeadmin")

user = UserModel.objects.create_user(
    email=test_tenant_email, password=test_tenant_password, is_staff=True)

print("Creating a test store Using subdomain [{}], name [{}]... to avoid this set AUTO_CREATE_TEST_TENANT to False".format(
    test_tenant_host, test_tenant_name))

try:
    if settings.AUTO_CREATE_TEST_TENANT:
        print("Creating a test store Using host [{}] and name [{}]... to avoid this set AUTO_CREATE_TEST_TENANT to False".format(test_tenant_host, test_tenant_name))
        # create tenant
        fqdn = provision_tenant(test_tenant_name, test_tenant_host, test_tenant_email, is_staff=True)
        print("Added Store: {}".format(test_tenant_name))
        print("Creating a normal user {} for Store: {}".format("user@leaky.com", test_tenant_name))
        user = UserModel.objects.create_user(email="user@leaky.com", password="password", is_staff=False)
        #tenant = Store.objects.filter(domain_url=fqdn).first()
        tenant = Store.objects.filter(domains__domain=fqdn).first()
        tenant.add_user(user, is_superuser=False, is_staff=False)
        print("User added")

    if settings.AUTO_CREATE_TEST_TENANT_GROUP:
        print("Creating a test corporation... to avoid this set AUTO_CREATE_TEST_TENANT_GROUP to False")
        corp = Corporation.objects.create(
            name=test_tenant_group_name,
            phone="1-555-5555"
        )
        user.corporation = corp
        user.save()
        print("Added Corporation: {}".format(test_tenant_group_name))

except Exception as e:
    print_exc()
    print(e)
    print("Unable to configure test schema.")

# extra data for testing
#user1 = UserModel.objects.create_user(email="user1@leaky.com", password="password", is_staff=False)
#tenant = Store.objects.filter(domain_url=fqdn).first()
#tenant.add_user(user1, is_superuser=False, is_staff=False)
#user1 = UserModel.objects.create_user(email="user1@leaky.com", password="password", is_staff=False)
#user2 = UserModel.objects.create_user(email="user2@leaky.com", password="password", is_staff=False)
#fqdn = provision_tenant("Test store1", "test1", "user1@leaky.com", is_staff=False)
#fqdn = provision_tenant("Test store2", "test2", "user2@leaky.com", is_staff=False)
#from customers.models import Store
#tenant2 = Store.objects.filter(domain_url=fqdn).first()
#tenant2.add_user(user1, is_superuser=False, is_staff=False)
