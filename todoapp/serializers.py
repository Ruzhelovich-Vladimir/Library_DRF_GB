from rest_framework.serializers import ModelSerializer
from .models import Project, ToDo
from libraryapp.serializers import AuthorSerializer


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'






