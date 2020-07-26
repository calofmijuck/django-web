from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    # Only owners are allowed to edit

    # SAFE_METHODS : GET, HEAD, OPTIONS
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
