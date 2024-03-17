from rest_framework.permissions import BasePermission 

class IsAdminOrCreateOnly(BasePermission):
    def has_permission(self , request , view):
        if request.method == 'POST':
            return True
        if request.user and request.user.is_superuser:
            return True
        return False
    