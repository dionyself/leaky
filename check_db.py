#!/usr/bin/env python
import os
import sys

import django
from django.db import connections

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leaky.settings")
django.setup()

db_conn = connections['default']
try:
    c = db_conn.cursor()
except Exception as ex:
    print("************ An exception of type {0} occurred. Arguments:\n{1!r}".
          format(type(ex).__name__, ex.args))
    sys.exit(1)
else:
    sys.exit(0)
