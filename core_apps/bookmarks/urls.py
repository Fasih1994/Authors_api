from django.urls import path

from .views import BookMarkCreateAPIView, BookMarkDestroyView

urlpatterns = [
    path(
        "bookmark_article/<uuid:article_id>/",
        BookMarkCreateAPIView.as_view(),
        name="bookmark_article",
    ),
    path(
        "remove_bookmark/<uuid:article_id>/",
        BookMarkDestroyView.as_view(),
        name="remove_bookmark",
    ),
]
