from rest_framework import permissions


class IsCurrentUserOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # The method is a safe method ('GET', 'HEAD', 'OPTIONS')
            return True
        else:
            # The method isn't a safe method ('DELETE', 'PUT')
            # Only owners are granted permissions for unsafe methods
            return obj.owner == request.user
