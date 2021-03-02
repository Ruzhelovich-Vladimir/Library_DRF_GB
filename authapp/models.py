from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)

class UserProfile(models.Model):

    MALE = 'M'
    FEMALE = "W"

    GENDER_CHOICES = {
        (MALE, 'M'),
        (FEMALE, 'Ж')
    }

    # user_name = models.OneToOneField(User, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    uuid = models.UUIDField(verbose_name='ид', primary_key=True, default=uuid4)
    user_name = models.CharField(verbose_name='имя пользователя', max_length=64)
    first_name = models.CharField(verbose_name='имя', max_length=64)
    last_name = models.CharField(verbose_name='фамилия', max_length=64)
    gender = models.CharField(blank=True, max_length=1,
                              choices=GENDER_CHOICES, verbose_name='пол')
    birthday_year = models.PositiveIntegerField(verbose_name='год рождения')
    email = models.CharField(verbose_name='E-Mail', unique=True, blank=False, max_length=64)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
