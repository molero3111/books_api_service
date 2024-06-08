from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from books_api_service.settings import LARAVEL_API_URL
from utils.http import validate_auth_header_format


class LoginView(APIView):
    def post(self, request):
        # Send a request to the login endpoint
        response = requests.post(f'{LARAVEL_API_URL}login', data=request.data,
                                 headers={
                                     'Accept': 'application/json'
                                 })
        # Return the response from the login endpoint to the client
        return Response(response.json(), status=response.status_code)


class LogoutView(APIView):
    def post(self, request):
        # Extract the Authorization header
        authorization_header_check = validate_auth_header_format(request)

        if not authorization_header_check['is_valid']:
            return authorization_header_check['response']

        # Send a request to the logout endpoint
        response = requests.post(f'{LARAVEL_API_URL}logout', headers={
            'Authorization': authorization_header_check.get("header"),
            'Accept': 'application/json'
        })
        # Return the response from the logout endpoint to the client
        return Response(response.json(), status=response.status_code)
