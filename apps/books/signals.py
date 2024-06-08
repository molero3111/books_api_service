from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.books.models import Book
from .tasks import update_published_books


@receiver(post_save, sender=Book)
def update_event(sender, instance, created, **kwargs):
    if created:
        update_published_books.delay(instance.author.id)


@receiver(post_delete, sender=Book)
def delete_event(sender, instance, **kwargs):
    update_published_books.delay(instance.author.id)
