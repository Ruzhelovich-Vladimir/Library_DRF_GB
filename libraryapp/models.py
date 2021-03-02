from django.db import models
from uuid import uuid4

class Author(models.Model):
    uuid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    first_name = models.CharField(verbose_name='имя', max_length=64)
    last_name = models.CharField(verbose_name='фамилия', max_length=64)
    birthday_year = models.PositiveIntegerField(verbose_name='год рождения')
