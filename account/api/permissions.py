from rest_framework.permissions import BasePermission

class NotAuthenticated(BasePermission):

    message = "you already have an account"
 
    def has_permission(self, request, view):

        print("has_permission is running.")
        return not request.user.is_authenticated
