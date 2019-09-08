from rest_framework.permissions import *

class IsAuthorOrReadOnly(BasePermission):
    """
    只允许俱乐部管理员修改但允许所有人读
    """

    def has_object_permission(self,request,view,obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user

class IsOwners(BasePermission):
    def has_object_permission(self,request,view,obj):
        return request.user.id == obj.id
