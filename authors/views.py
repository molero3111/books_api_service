from rest_framework.pagination import PageNumberPagination
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from authors.models import Author
from authors.serializers import AuthorSerializer


class CustomAuthorPagination(PageNumberPagination):  # TODO: create reusable class
    page_size = 50  # sets the default number of records to retrieve

    # sets the query param name in case the request needs
    # to show fewer records than default value
    page_size_query_param = 'page_size'

    # sets maximum number of records to retrieve if it is
    # specified it on the query param as page_size
    max_page_size = 50


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all().order_by('-id')  # Order by `id` descending
    serializer_class = AuthorSerializer
    pagination_class = CustomAuthorPagination

    # permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):  # create reusable destroy method
        # Retrieve the user object before deletion
        author_to_delete = self.get_object()
        user_data = AuthorSerializer(author_to_delete).data
        author_to_delete.delete()
        return Response(
            {
                "message": "User was deleted successfully.",
                "deleted_author": user_data
            },
            status=HTTP_200_OK
        )
