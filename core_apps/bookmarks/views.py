import logging
from uuid import UUID

from django.db import IntegrityError
from rest_framework import generics, permissions, status
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.response import Response

from core_apps.articles.models import Article

from .exceptions import AlreadyBookmarkedArticle
from .models import BookMark
from .serializers import BookMarkSerializer

logger = logging.getLogger(__name__)


class BookMarkCreateAPIView(generics.CreateAPIView):
    queryset = BookMark.objects.all()
    serializer_class = BookMarkSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        article_id = self.kwargs.get("article_id")
        if article_id:
            try:
                article = Article.objects.get(id=article_id)
            except Article.DoesNotExist:
                raise ValidationError("Invalid article_id provided.")
        else:
            raise ValidationError("article_id is required.")

        try:
            serializer.save(user=self.request.user, article=article)
        except IntegrityError:
            raise AlreadyBookmarkedArticle


class BookMarkDestroyView(generics.DestroyAPIView):
    queryset = BookMark.objects.all()
    lookup_field = "article_id"
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        article_id = self.kwargs.get("article_id")

        try:
            UUID(article_id.hex, version=4)
        except ValueError:
            raise ValidationError("Invalid article_id provided")

        try:
            bookmark = BookMark.objects.get(user=user, article__id=article_id)

        except BookMark.DoesNotExist:
            raise NotFound("Bookmark is not found or is not belong to you.")

        return bookmark

    def perform_destroy(self, instance):
        user = self.request.user
        if instance.user != user:
            raise ValidationError("You cannot delete a bookmark that is not yours.")

        instance.delete()
