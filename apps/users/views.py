
from rest_framework.viewsets import ModelViewSet

from apps.authentication.permissions import IsValidToken
from apps.users.models import User
from apps.users.serializers import UserSerializer
from utils.http import get_delete_response
from utils.pagination import PaginationSettings


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-id')  # Order by `id` descending
    serializer_class = UserSerializer
    pagination_class = PaginationSettings
    permission_classes = [IsValidToken]

    def destroy(self, request, *args, **kwargs):
        return get_delete_response(self)
