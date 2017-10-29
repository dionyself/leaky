#!/usr/bin/env python
import os
from traceback import print_exc
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leaky.settings")
django.setup()

from django.conf import settings
from customers.models import Client

host = settings.TEST_TENANT_HOST
schema_name = "test"
client_name = "Test Client"
print("Creating a test client Using host [{}], with schema [{}] and name [{}]... to avoid this set AUTO_CREATE_TEST_TENANT to False".format(
    host, schema_name, client_name))

try:
    if settings.AUTO_CREATE_TEST_TENANT:
        if not Client.objects.filter(schema_name=schema_name).first():
            tenant = Client.objects.create(
                domain_url=host,
                schema_name=schema_name,
                name=client_name,
                )
            print("Added Client: {}".format(client_name))
except Exception as e:
    print_exc()
    print(e)
    print("Unable to configure test schema.")
