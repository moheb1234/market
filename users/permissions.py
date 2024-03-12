from rest_framework.permissions import BasePermission

class IsProfileOwner(BasePermission):
    def has_object_permission(self ,request , view , obj):
        user  =request.user
        if user.profile == obj:
            return True
        return False