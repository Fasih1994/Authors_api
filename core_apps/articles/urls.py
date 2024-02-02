from django.urls import path
from .views import ArticleListCreateView, ArticleRetieveUpdateDestroyView


urlpatterns = [
    path('', ArticleListCreateView.as_view(), name='article-list-create'),
    path('<uuid:id>/', ArticleRetieveUpdateDestroyView.as_view(),
         name='article-retrieve-update-destroy'),
]
