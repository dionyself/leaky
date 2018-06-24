
class PermissionsMiddleware(object):

    def resolve(self, next, root, info, **args):

        #'get_all_permissions', 'get_deferred_fields', 'get_email_field_name',
        #'get_full_name', 'get_group_permissions', 'get_next_by_created_at',
        #'get_next_by_updated_at', 'get_previous_by_created_at',
        #'get_previous_by_updated_at', 'get_session_auth_hash', 'get_short_name',
        #'get_username', 'has_module_perms', 'has_perm', 'has_perms',
        #'has_tenant_permissions', 'has_usable_password', 'has_verified_email',
        #'id', 'is_active', 'is_anonymous', 'is_authenticated', 'is_deleted',
        #'is_staff', 'is_superuser', 'is_verified', 'last_login', 'usertenantpermissions'
        # print_user_credentials(info.context.user)
        # tenant = get_current_tenant()
        # schema = get_public_schema_name()
        # info.context.user.has_perm("can_read_corporation_")

        permission_name = ""
        if info.operation.operation == "query":
            permission_name = "%s__%s" % (info.operation.selection_set.selections[0].name.value, info.field_name)
        elif info.operation.operation == "mutation":
            permission_name = info.field_name
        if info.context.user.has_perms([permission_name]):
            print("user has %s permissions" % permission_name)
        else:
            print("user has no %s permissions" % permission_name)
        return next(root, info, **args)
