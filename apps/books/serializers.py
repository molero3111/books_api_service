from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from apps.authors.models import Author
from apps.books.models import Book


class BookSerializer(ModelSerializer):
    author = SlugRelatedField(
        queryset=Author.objects.all(),
        slug_field='id'
    )

    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'published_at']
