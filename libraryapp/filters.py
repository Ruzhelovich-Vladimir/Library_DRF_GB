from django_filters import rest_framework as filters
from .models import Article

class ArticleFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')  # часть совподений
    class Meta:
        model = Article
        fields = ['name']