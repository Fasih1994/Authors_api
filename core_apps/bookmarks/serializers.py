from rest_framework import serializers

from .models import BookMark


class BookMarkSerializer(serializers.ModelSerializer):
    article_title = serializers.CharField(source="article.title", read_only=True)
    user_first_name = serializers.CharField(source="user.first_name", read_only=True)

    class Meta:
        model = BookMark
        fields = ["id", "user_first_name", "article_title", "created_at"]
        read_only_fields = ["user"]
