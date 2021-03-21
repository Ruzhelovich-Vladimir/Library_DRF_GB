from django.urls import  path, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from todoapp.views import AuthorViewSet, ToDoViewSet, ProjectsViewSet

#schema_view = get_swagger_view(title='Swagger')

app_name = 'todoapp'

router = DefaultRouter()
router.register('projects', ProjectsViewSet, basename='project')
router.register('todo', ToDoViewSet, basename='todo')
router.register('author', AuthorViewSet, basename='author')
#router.register('swagger', schema_view, basename='project')

urlpatterns = [
    path('', include(router.urls))
]