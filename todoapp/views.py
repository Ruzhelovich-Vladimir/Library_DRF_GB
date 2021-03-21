from rest_framework import mixins
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from rest_framework.pagination import LimitOffsetPagination

from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer
from .filters import ProjectFilter, ToDoFilter

from libraryapp.models import Author
from libraryapp.serializers import AuthorSerializer

class LimitOffsetPagination_10(LimitOffsetPagination):
    default_limit = 10

class LimitOffsetPagination_20(LimitOffsetPagination):
    default_limit = 20

class ProjectsViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    pagination_class = LimitOffsetPagination_10

class AuthorViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, GenericViewSet):
    '''
    есть возможность просмотра списка и каждого пользователя в отдельности,
    можно вносить изменения, нельзя удалять и создавать;
    '''
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

class ToDoViewSet(ModelViewSet):
    '''
    модель ToDo: доступны все варианты запросов; при удалении не удалять ToDo,
    а выставлять признак, что оно закрыто; добавить фильтрацию по проекту;
    для постраничного вывода установить размер страницы 20.
    '''
    queryset = ToDo.objects.all()
    serializer_class = ToDoModelSerializer
    pagination_class = LimitOffsetPagination_20
    filterset_class = ToDoFilter

    def perform_destroy(self, instance): # Решил перепределить этот метод
        instance.is_active = not instance.is_active
        instance.save()
