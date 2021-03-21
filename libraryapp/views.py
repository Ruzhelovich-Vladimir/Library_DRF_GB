from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    get_object_or_404
from rest_framework.views import APIView
from .models import Author, Biography, Article, Book
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, BiographySerializer, ArticleSerializer, BookSerializer, \
    ArticleModelSerializer

from rest_framework import viewsets, mixins
from .filters import ArticleFilter

class ArticleAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True, default=[])
        return Response(serializer.data)

# @api_view(['GET'])
# @renderer_classes([JSONRenderer])
# def article_view(request):
#     articles = Article.objects.all()
#     serializer = ArticleSerializer(Article, many=True)
#     return  Response(serializer.data)

#Generic
class ArticleCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    # Использую без гиперлинка
    serializer_class = ArticleModelSerializer

#Generic
class ArticleListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer

#Generic
class ArticleKwargsFilterView(ListAPIView):
    serializer_class = ArticleModelSerializer

    def get_queryset(self):
        #Фильтрация по контексту
        name = self.kwargs['name']
        return Article.objects.filter(name__contains=name)
        # Пример http://127.0.0.1:8000/filters/kwargs/and/


#Generic
class ArticleRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


#Generic
class ArticleDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    # Использую без гиперлинка
    serializer_class = ArticleModelSerializer


#Generic
class ArticleUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Article.objects.all()
    # Использую без гиперлинка
    serializer_class = ArticleModelSerializer

#ViewSets
class ArticleViewSets(viewsets.ViewSet):
    renderer_classes = [JSONRenderer]

    @action(detail=True, methods=['get'])
    def article_text_only(self,request, pk=None):
        article = get_object_or_404(Article,pk=pk)
        return Response({'article.text': article.text})
        '''
        Кастомный метод
        Метод изменяет вывод объект 
        на адрес: http://127.0.0.1:8000/view/bases/af720872-8831-4223-a57e-d807aebd8522/article_text_only/
        {"article.text":"Haskell features a type system with type inference and lazy evaluation. Erlang is known for its designs that are well suited for systems. He looked inquisitively at his keyboard and wrote another sentence. Messages can be sent to and received from ports, but these messages must obey the so-called \"port protocol.\" Do you have any idea why this is not working? Do you have any idea why this is not working? It is also a garbage-collected runtime system. Messages can be sent to and received from ports, but these messages must obey the so-called \"port protocol.\" Make me a sandwich. Atoms can contain any character if they are enclosed within single quotes and an escape convention exists which allows any character to be used within an atom. Haskell features a type system with type inference and lazy evaluation. Its main implementation is the Glasgow Haskell Compiler. The sequential subset of Erlang supports eager evaluation, single assignment, and dynamic typing. Erlang is a general-purpose, concurrent, functional programming language. Do you come here often? Type classes first appeared in the Haskell programming language. Atoms are used within a program to denote distinguished values. The syntax {D1,D2,...,Dn} denotes a tuple whose arguments are D1, D2, ... Dn. Ports are created with the built-in function open_port. Do you come here often? The sequential subset of Erlang supports eager evaluation, single assignment, and dynamic typing. The Galactic Empire is nearing completion of the Death Star, a space station with the power to destroy entire planets. I don't even care. Any element of a tuple can be accessed in constant time. The arguments can be primitive data types or compound data types. It is also a garbage-collected runtime system. The Galactic Empire is nearing completion of the Death Star, a space station with the power to destroy entire planets. Its main implementation is the Glasgow Haskell Compiler. They are written as strings of consecutive alphanumeric characters, the first character being lowercase. Haskell is a standardized, general-purpose purely functional programming language, with non-strict semantics and strong static typing. In 1989 the building was heavily damaged by fire, but it has since been restored. Erlang is a general-purpose, concurrent, functional programming language. Its main implementation is the Glasgow Haskell Compiler. Tuples are containers for a fixed number of Erlang data types. He looked inquisitively at his keyboard and wrote another sentence. Make me a sandwich. In 1989 the building was heavily damaged by fire, but it has since been restored. Ports are used to communicate with the external world. Haskell is a standardized, general-purpose purely functional programming language, with non-strict semantics and strong static typing. Erlang is known for its designs that are well suited for systems. Atoms are used within a program to denote distinguished values. Any element of a tuple can be accessed in constant time. Haskell is a standardized, general-purpose purely functional programming language, with non-strict semantics and strong static typing. They are written as strings of consecutive alphanumeric characters, the first character being lowercase. Tuples are containers for a fixed number of Erlang data types. They are written as strings of consecutive alphanumeric characters, the first character being lowercase. Initially composing light-hearted and irreverent works, he also wrote serious, sombre and religious pieces beginning in the 1930s. The Galactic Empire is nearing completion of the Death Star, a space station with the power to destroy entire planets. Any element of a tuple can be accessed in constant time. They are written as strings of consecutive alphanumeric characters, the first character being lowercase."}
        '''


    def list(self, request):

        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
        '''
        http://127.0.0.1:8000/view/bases/
        список всех объектов
        '''


    def retrieve(self, request, pk=None):

        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
        '''
        http://127.0.0.1:8000/view/bases/abf2aea0-ceb8-4dd2-aa78-c4e2981488cc/
        список одного объкта
        {"uuid":"abf2aea0-ceb8-4dd2-aa78-c4e2981488cc","name":"The syntax {D1,D2,...,Dn} denotes a tuple whose arguments are D1, D2, ... Dn.","text":"In 1989 the building was heavily damaged by fire, but it has since been restored. The arguments can be primitive data types or compound data types. The arguments can be primitive data types or compound data types. The Galactic Empire is nearing completion of the Death Star, a space station with the power to destroy entire planets. Type classes first appeared in the Haskell programming language. The syntax {D1,D2,...,Dn} denotes a tuple whose arguments are D1, D2, ... Dn. The syntax {D1,D2,...,Dn} denotes a tuple whose arguments are D1, D2, ... Dn. Atoms are used within a program to denote distinguished values. Where are my pants? Atoms are used within a program to denote distinguished values. Atoms are used within a program to denote distinguished values. Erlang is a general-purpose, concurrent, functional programming language. Where are my pants? In 1989 the building was heavily damaged by fire, but it has since been restored. I don't even care. Do you come here often? Ports are used to communicate with the external world. Erlang is known for its designs that are well suited for systems. Erlang is a general-purpose, concurrent, functional programming language. Do you have any idea why this is not working? Where are my pants? In 1989 the building was heavily damaged by fire, but it has since been restored. They are written as strings of consecutive alphanumeric characters, the first character being lowercase. Make me a sandwich. Make me a sandwich. Tuples are containers for a fixed number of Erlang data types. I don't even care. Make me a sandwich. Any element of a tuple can be accessed in constant time. Atoms are used within a program to denote distinguished values. Make me a sandwich. Erlang is a general-purpose, concurrent, functional programming language. It is also a garbage-collected runtime system. He looked inquisitively at his keyboard and wrote another sentence. She spent her earliest years reading classic literature, and writing poetry. The Galactic Empire is nearing completion of the Death Star, a space station with the power to destroy entire planets. Any element of a tuple can be accessed in constant time. Do you come here often? Type classes first appeared in the Haskell programming language. Ports are created with the built-in function open_port. Atoms are used within a program to denote distinguished values. In 1989 the building was heavily damaged by fire, but it has since been restored. Messages can be sent to and received from ports, but these messages must obey the so-called \"port protocol.\" I don't even care. They are written as strings of consecutive alphanumeric characters, the first character being lowercase. I don't even care. The arguments can be primitive data types or compound data types. In 1989 the building was heavily damaged by fire, but it has since been restored. Where are my pants? Tuples are containers for a fixed number of Erlang data types.","author_uuid":"a3f5d009-3d94-41bb-b841-7391f0e1538f"}
        '''

"""
Custom ViewSet

Наследуя 
"""
class ArticleCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                          mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    """наследуя те методы (миксины), которые отвечаю за rest запросы мы можем 
    ограничить права, используя эти методы или исключить эти ментоды
    класс ModelViewSet наследуюет все возможные миксины - этот метод же является аналогом ModelViewSet,
    но уже кастомный 
    """

#ModelViewSet
class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = ArticleSerializer


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ArticleDjangoFilterViewSet(viewsets.ModelViewSet):
    # Настройка стандартные фильтра DRF
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['name', 'text']

class ArticleCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_class = ArticleFilter # Кастомный фильтр
