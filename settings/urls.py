from django.contrib import admin
from django.urls import  path, include
from rest_framework.routers import DefaultRouter
from libraryapp.views import AuthorModelViewSet, BiographyViewSet, ArticleViewSet,BookViewSet
from authapp.views import UserProfileModelViewSet
from todoapp.views import ProjectViewSet, ToDoViewSet
from rest_framework_swagger.views import get_swagger_view

app_name = 'libraryapp'

schema_view = get_swagger_view(title='Library API')

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('biographies', BiographyViewSet)
router.register('articles', ArticleViewSet)
router.register('books', BookViewSet)
router.register('projects', ProjectViewSet)
router.register('todo', ToDoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('swagger/', schema_view)

]
