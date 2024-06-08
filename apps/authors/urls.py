from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.authors.views import AuthorViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls), name='author_crud')
]