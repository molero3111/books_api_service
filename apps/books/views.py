from rest_framework.viewsets import ModelViewSet

from apps.authentication.permissions import IsValidToken
from apps.books.models import Book
from apps.books.serializers import BookSerializer
from utils.http import get_delete_response
from utils.pagination import PaginationSettings


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().order_by('-id')  # Order by `id` descending
    serializer_class = BookSerializer
    pagination_class = PaginationSettings
    permission_classes = [IsValidToken]

    def destroy(self, request, *args, **kwargs):
        return get_delete_response(self)
