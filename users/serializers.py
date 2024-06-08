from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from users.models import User, Role


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name']


class UserSerializer(ModelSerializer):
    role = SlugRelatedField(
        queryset=Role.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'password', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }
