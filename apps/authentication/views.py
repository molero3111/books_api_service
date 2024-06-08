from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from books_api_service.settings import LARAVEL_API_URL


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
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return Response({'error': 'Authorization header is missing'}, status=400)

        # Check if the header starts with 'Bearer '
        if not auth_header.startswith('Bearer '):
            return Response({'error': 'Invalid token format'}, status=400)

        # Extract the token
        token = auth_header.split(' ')[1]
        # Send a request to the logout endpoint
        response = requests.post(f'{LARAVEL_API_URL}logout', headers={
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json'
        })
        # Return the response from the logout endpoint to the client
        return Response(response.json(), status=response.status_code)
