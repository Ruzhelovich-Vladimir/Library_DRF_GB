from django.db import models
from uuid import uuid4

class Author(models.Model):

    uuid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    first_name = models.CharField(verbose_name='имя', max_length=64)
    last_name = models.CharField(verbose_name='фамилия', max_length=64)
    birthday_year = models.PositiveIntegerField(verbose_name='год рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Biography(models.Model):
    uuid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    author = models.OneToOneField(Author, verbose_name='автор', on_delete=models.DO_NOTHING)
    text = models.TextField(verbose_name='биография')

class Book(models.Model):
    uuid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    name = models.CharField(max_length=128, verbose_name='наименование книги', blank=False)
    author = models.OneToOneField(Author, verbose_name='автор', on_delete=models.DO_NOTHING, blank=False)

class Article(models.Model):
    name = models.CharField(max_length=128, verbose_name='наименование статьи', blank=False)
    author = models.OneToOneField(Author, verbose_name='автор', on_delete=models.DO_NOTHING, blank=False)




