from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Safe method GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return False

class WriteOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #Safe method GET, HEAD or OPTIONS requests.
        if request.method =='POST':
            return True
        return False

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner
        return obj.owner == request.user
