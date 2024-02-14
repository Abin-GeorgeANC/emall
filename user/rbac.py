#emall/user/rbac


from rest_framework import permissions


class IsManager(permissions.BasePermission):

    def has_permission(self,request):

        try:
            user_scope=request.user.user_scope
            if user_scope== 'MANAGER':
                return True
            else :
                return False
        except Exception as ex:
            return False