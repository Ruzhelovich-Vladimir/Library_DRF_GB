from django.db import models
from uuid import uuid4
from django.utils.timezone import now
from authapp.models import UserApp

class Author(models.Model):
    uuid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    # При удалении пользователя авторов мы не должны потерять, поэтому автор может не привязан к пользователю
    user = models.OneToOneField(UserApp, verbose_name='пользователь', null=True, on_delete=models.DO_NOTHING)
    first_name = models.CharField(verbose_name='имя', max_length=64)
    last_name = models.CharField(verbose_name='фамилия', max_length=64)
    birthday_year = models.PositiveIntegerField(verbose_name='год рождения')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Biography(models.Model):
    uuid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    author = models.OneToOneField(Author, name='author_uuid', verbose_name='автор', on_delete=models.DO_NOTHING)
    text = models.TextField(verbose_name='биография')

class Book(models.Model):
    uuid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    name = models.CharField(max_length=128, verbose_name='наименование книги', blank=False)
    author = models.ForeignKey(Author, verbose_name='автор', name='author_uuid', on_delete=models.DO_NOTHING, blank=False)

class Article(models.Model):
    uuid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    name = models.CharField(max_length=128, verbose_name='наименование статьи', blank=False)
    text = models.TextField(verbose_name='текст статьи')
    author = models.ForeignKey(Author, verbose_name='автор', name='author', on_delete=models.DO_NOTHING, blank=False)
    # created_at = models.DateTimeField(verbose_name='создан', default=now())

    def __str__(self):
        return self.name






