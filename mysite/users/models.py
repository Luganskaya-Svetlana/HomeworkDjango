from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField('день рождения', blank=True)


class Meta:
    verbose_name = 'профиль'
    verbose_name_plural = 'профили'


def __str__(self):
    return f'{self.user.name} (расширенный профиль)'
