from django.urls import path
from .views import export_authors_books

urlpatterns = [
    # Other URL patterns
    path('authors/books/', export_authors_books, name='export-authors-books'),
]
