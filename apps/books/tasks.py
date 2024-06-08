from celery import shared_task
from apps.books.models import Book
from apps.authors.models import Author


@shared_task
def update_published_books(author_id):
    author = Author.objects.get(pk=author_id)
    book_count = Book.objects.filter(author=author).count()
    author.published_books = book_count
    author.save()
