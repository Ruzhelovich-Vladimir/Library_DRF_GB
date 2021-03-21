from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, Serializer
from libraryapp.models import Author, Biography, Article, Book

class AuthorNameSerializer(ModelSerializer):
   class Meta:
       model = Author
       # fields = ['uuid', 'first_name', 'last_name']
       fields = '__all__'

class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
        # exclude = ['url', 'user']



class BiographySerializer(ModelSerializer):
    author = AuthorNameSerializer()
    class Meta:
        model = Biography
        fields = '__all__'
        # exclude = ['url']

class ArticleModelSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class BookSerializer(ModelSerializer):
    author = AuthorNameSerializer()
    class Meta:
        model = Book
        fields = '__all__'
        # exclude = ['url']