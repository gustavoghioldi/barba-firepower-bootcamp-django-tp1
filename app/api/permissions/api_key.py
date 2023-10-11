from rest_framework.permissions import BasePermission, SAFE_METHODS
from app.settings import API_KEY
class ApiKey(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(request.headers.get("x-api-key") == API_KEY )