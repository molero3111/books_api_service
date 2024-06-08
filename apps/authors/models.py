from django.db import models

from apps.users.models import User


class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(unique=True, max_length=100)
    published_books = models.SmallIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authors'
