from django.contrib import admin
from django.urls import  path, include
from rest_framework.routers import DefaultRouter
from libraryapp.views import AuthorModelViewSet, BiographyViewSet, ArticleViewSet, BookViewSet, \
    ArticleAPIView, ArticleRetrieveAPIView, ArticleCreateAPIView, ArticleListAPIView, ArticleDestroyAPIView, \
    ArticleUpdateAPIView, ArticleViewSets, ArticleKwargsFilterView, ArticleCustomDjangoFilterViewSet, \
    ArticleDjangoFilterViewSet
from rest_framework_swagger.views import get_swagger_view

app_name = 'libraryapp'

schema_view = get_swagger_view(title='Library API')

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('biographies', BiographyViewSet)
router.register('articles', ArticleViewSet)
router.register('books', BookViewSet)
router.register('base', ArticleViewSet, basename='article')
router.register('bases', ArticleViewSets, basename='article')

filter_router = DefaultRouter()
filter_router.register('django', ArticleDjangoFilterViewSet)
filter_router.register('customdjango', ArticleCustomDjangoFilterViewSet)

urlpatterns = [
    # path('view/', include(router.urls)),
    # path('view/api-view/', ArticleAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todo/', include('todoapp.urls')), # Мне больше симпозизирует, когда urls приложение описаны в самом приложении.
    path('view/', include(router.urls)),
    # path('generic/create/', ArticleCreateAPIView.as_view()),
    # path('generic/list/', ArticleListAPIView.as_view()),
    # # path('generic/retrieve/<uuid:pk>/', ArticleRetrieveAPIView.as_view()),
    # path('generic/destroy/<uuid:pk>/', ArticleDestroyAPIView.as_view()),
    # path('generic/update/<uuid:pk>/', ArticleUpdateAPIView.as_view()),
    path('filters/', include(filter_router.urls)),
    # path('filters/kwargs/<str:name>/', ArticleKwargsFilterView.as_view()),
    path('swagger/', schema_view)
]
