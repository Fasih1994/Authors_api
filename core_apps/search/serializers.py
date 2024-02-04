from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import ArticleDocument


class ArticleElasticSearchSerializer(DocumentSerializer):
    class Meta:
        document = ArticleDocument
        fields = [
            "id",
            "author",
            "title",
            "slug",
            "tags",
            "estimated_time" "description",
            "body",
            "created_at",
        ]
