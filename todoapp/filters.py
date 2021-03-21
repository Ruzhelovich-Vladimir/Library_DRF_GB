from django_filters import rest_framework as filters
from .models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')  # часть совподений
    class Meta:
        model = Project
        fields = ['name']

class ToDoFilter(filters.FilterSet):
    text = filters.CharFilter(lookup_expr='contains')  # часть совподений
    created_gt = filters.DateFilter(field_name='created_at', lookup_expr='gt')
    created_lt = filters.DateFilter(field_name='created_at', lookup_expr='lt')

    class Meta:
        model = ToDo
        fields = ['project', 'text']


