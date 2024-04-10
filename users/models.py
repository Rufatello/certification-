from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта', max_length=70)
    country = models.CharField(verbose_name='Страна', max_length=70)
    city = models.CharField(verbose_name='Город', max_length=70)
    street = models.CharField(verbose_name='Улица', max_length=70)
    house_number = models.PositiveIntegerField(verbose_name='Номер дома')
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'