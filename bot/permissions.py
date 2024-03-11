from rest_framework.permissions import BasePermission


class IsBotOwner(BasePermission):
    def has_object_permission(self , request , view , obj):
        user = request.user
        if obj.strategy.user == user:
            return True
        return False