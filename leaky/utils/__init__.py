def print_user_credentials(user):
    #print("######### dir(user) %s" % dir(user))
    print("######### is_staff %s " % user.is_staff)
    print("######### is_superuser %s " % user.is_superuser)
    #print("######### get_group_permissions %s " % user.get_group_permissions())
    #print("######### type(usertenantpermissions) %s " % type(user.usertenantpermissions))
    #print("######### groups %s " % user.groups)
    #print("######### user_permissions %s " % user.user_permissions)
    #print("######### usertenantpermissions.is_staff %s " % user.usertenantpermissions.is_staff)
    #print("######### usertenantpermissions.is_superuser %s " % user.usertenantpermissions.is_superuser)
    print("######### usertenantpermissions.get_all_permissions %s " % user.usertenantpermissions.get_all_permissions())
    print("######### usertenantpermissions.get_group_permissions %s " % user.usertenantpermissions.get_group_permissions())
    #print("######### type(usertenantpermissions.groups) %s " % type(user.usertenantpermissions.groups))
    #print("######### type(usertenantpermissions.user_permissions) %s " % type(user.usertenantpermissions.user_permissions))
    #rint("######### usertenantpermissions.groups %s " % dir(user.usertenantpermissions.groups))
    #print("######### usertenantpermissions.user_permissions %s " % user.usertenantpermissions.user_permissions)
