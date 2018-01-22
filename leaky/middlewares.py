from tenant_users.tenants.utils import get_current_tenant
from django.db import connection
from customers.models import Corporation
from tenant_schemas.utils import get_public_schema_name, get_tenant_model, schema_context
from leaky.utils import print_user_credentials


class PermissionsMiddleware(object):

    def resolve(self, next, root, info, **args):
        return next(root, info, **args)

        """
            'get_all_permissions', 'get_deferred_fields', 'get_email_field_name',
            'get_full_name', 'get_group_permissions', 'get_next_by_created_at',
            'get_next_by_updated_at', 'get_previous_by_created_at',
            'get_previous_by_updated_at', 'get_session_auth_hash', 'get_short_name',
            'get_username', 'has_module_perms', 'has_perm', 'has_perms',
            'has_tenant_permissions', 'has_usable_password', 'has_verified_email',
            'id', 'is_active', 'is_anonymous', 'is_authenticated', 'is_deleted',
            'is_staff', 'is_superuser', 'is_verified', 'last_login', 'usertenantpermissions'
        """

        # print_user_credentials(info.context.user)
        # tenant = get_current_tenant()
        # schema = get_public_schema_name()
        # info.context.user.has_perm("can_read_corporation_")

        allow = False
        if info.operation.operation == 'query':
            if True:  #with schema_context(get_public_schema_name()):
                if info.context.user.has_perm("can_read_corporation_%s" % "tenant.corporation_id"):
                    allow = True
                if info.context.user.has_perm("can_read_store_%s" % "tenant.id"):
                    allow = True
            if info.context.user.has_perm("can_read_%s" % info.field_name):
                allow = True
            if allow:
                return next(root, info, **args)
            else:
                if "GraphQL" in type(info.return_type).__name__:
                    return next(root, info, **args)
                return None

        else:
            return next(root, info, **args)
