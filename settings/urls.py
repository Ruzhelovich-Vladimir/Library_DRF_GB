from django.contrib import admin
from django.urls import  path, include
from rest_framework.routers import DefaultRouter
from libraryapp.views import AuthorModelViewSet
from authapp.views import UserProfileModelViewSet
from rest_framework_swagger.views import get_swagger_view

app_name = 'libraryapp'

schema_view = get_swagger_view(title='Library API')

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('users', UserProfileModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('', schema_view)

]
