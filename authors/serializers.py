from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from authors.models import Author
from users.models import User


class AuthorSerializer(ModelSerializer):
    user = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Author
        fields = ['id', 'user', 'nickname', 'published_books']
