from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED
from rest_framework.viewsets import ModelViewSet

from apps.authentication.permissions import IsValidToken
from apps.authors.models import Author
from apps.authors.serializers import AuthorSerializer
from utils.http import get_delete_response
from utils.pagination import PaginationSettings


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all().order_by('-id')  # Order by `id` descending
    serializer_class = AuthorSerializer
    pagination_class = PaginationSettings
    permission_classes = [IsValidToken]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            self.perform_create(serializer)
        except IntegrityError:
            return Response(
                {"error": "This user already has an associated author."},
                status=HTTP_400_BAD_REQUEST
            )

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        return get_delete_response(self)
