from rest_framework.permissions import BasePermission
import requests
from rest_framework.exceptions import PermissionDenied

from books_api_service.settings import LARAVEL_API_URL
from utils.http import validate_auth_header_format


class IsValidToken(BasePermission):
    """
    Custom permission to authenticate using an external service.
    """

    def has_permission(self, request, view):
        # Extract the Bearer token from the request headers
        authorization_header_check = validate_auth_header_format(request)

        if not authorization_header_check['is_valid']:
            raise PermissionDenied('Authorization header is missing.')

        # Make the request to the external service
        response = requests.post(
            f'{LARAVEL_API_URL}authorize-service-request',
            headers={'Authorization': authorization_header_check.get("header")}
        )

        # Check the response status code
        if response.status_code == 201:
            return True
        else:
            raise PermissionDenied('Not authorized by the external service.')
