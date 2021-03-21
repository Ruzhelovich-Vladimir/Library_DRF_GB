from django.db import models
from libraryapp.models import Author
from uuid import uuid4

class Project(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(verbose_name='наименование проекта', max_length=50, unique=True)
    authors = models.ManyToManyField(Author, verbose_name='пользователь', name='authors')
    repository_url = models.URLField(verbose_name='url репозитория проекта')


    def __str__(self):
        return self.name

class ToDo(models.Model):
    project = models.ForeignKey(Project, verbose_name='проект', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='текст')
    author = models.ForeignKey(Author, verbose_name='пользователь', name='author', on_delete=models.PROTECT)
    is_active = models.BooleanField(default='признак активации')
    created_at = models.DateTimeField(verbose_name='создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='обновлено', auto_now=True)



