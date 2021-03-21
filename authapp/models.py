from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from datetime import timedelta


class User(AbstractUser):
    pass

# TODO Реализовать:
#   * разраничение прав по группам
#   * создавать группу Administrator для API автомаически (для будующей админки)
#   * реализовать скрипт создания супер пользователя для проекта
#   * реализовать скрипты для создания и предоставления прав пользователю (пока без адиминки)
class GroupApp(models.Model):
    name = models.CharField(verbose_name='имя группы', primary_key=True, null=False, db_index=True,
                            max_length=64)
    descriptions = models.CharField(verbose_name='описание', null=True, max_length=128)

# TODO реализовать получение/обновление токена для доступа и токена для обновления,
#  токена для доступа. В длальнйшем использовать NoSql
class UserApp(models.Model):
    login = models.CharField(verbose_name='логин', max_length=64, primary_key=True,
                             null=False, db_index=True)
    password = models.CharField(verbose_name='хеш пароля', max_length=64)
    group = models.ForeignKey(GroupApp, verbose_name='группа', null=True,
                              on_delete=models.DO_NOTHING)

    access_token = models.CharField(verbose_name='токен доступа', max_length=128, blank=True)
    access_token_expires = models.DateTimeField(verbose_name='срок действия токена доступа',
                                                default=(now() + timedelta(hours=48)))
    refresh_token = models.CharField(verbose_name='токен обновления', max_length=128, blank=True)
    refresh_token_expires = models.DateTimeField(verbose_name='срок действия токена обновления',
                                                 default=(now() + timedelta(hours=48)))

    def is_access_token_expires(self):
        return now() <= self.access_token_expires

    def is_refresh_token_expires(self):
        return now() <= self.refresh_token_expires
