from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, ValidationError

from apps.authors.models import Author
from apps.users.models import User


class AuthorSerializer(ModelSerializer):
    user = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='id'
    )

    def validate_user(self, value):
        if Author.objects.filter(user=value).exists():
            raise ValidationError("This user already has an associated author.")
        return value

    class Meta:
        model = Author
        fields = ['id', 'user', 'nickname', 'published_books']
