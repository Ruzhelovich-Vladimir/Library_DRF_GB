from rest_framework.serializers import HyperlinkedModelSerializer, Serializer
from .models import Project, ToDo
from libraryapp.serializers import AuthorSerializer


class ProjectModelSerializer(HyperlinkedModelSerializer):
    # authors = AuthorSerializer()
    class Meta:
        model = Project
        exclude = ['url']

class ToDoModelSerializer(HyperlinkedModelSerializer):
    #project = ProjectModelSerializer()
    #author = AuthorSerializer()
    class Meta:
        model = ToDo
        exclude = ['url']





