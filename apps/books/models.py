from django.db import models

from apps.authors.models import Author


class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'
