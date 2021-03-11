from rest_framework.serializers import HyperlinkedModelSerializer
from libraryapp.models import Author, Biography, Article, Book

class AuthorSerializer(HyperlinkedModelSerializer):
   class Meta:
       model = Author
       exclude = ['url']

class BiographySerializer(HyperlinkedModelSerializer):
   author = AuthorSerializer()
   class Meta:
       model = Biography
       exclude = ['url']

class ArticleSerializer(HyperlinkedModelSerializer):
   author = AuthorSerializer()
   class Meta:
       model = Article
       exclude = ['url']

class BookSerializer(HyperlinkedModelSerializer):
   author = AuthorSerializer()
   class Meta:
       model = Book
       exclude = ['url']