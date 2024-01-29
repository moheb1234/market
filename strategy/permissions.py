from rest_framework.permissions import BasePermission 

class IsStrategyOwner(BasePermission):
    def has_object_permission(self , request , view , obj):
        user = request.user
        if obj.user == user:
            return True
        return False
            