from Core.models import PublishedBaseModel, SlugBaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import validate_perfect


class Tag(PublishedBaseModel, SlugBaseModel):
    name = models.CharField(name='name', verbose_name='Название тэга',
                            max_length=150,
                            help_text='Максимум 150 символов',
                            default='')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name


class Category(PublishedBaseModel, SlugBaseModel):
    name = models.CharField(name='name', verbose_name='Название категории',
                            max_length=150,
                            help_text='Максимум 150 символов',
                            default='')
    weight = models.IntegerField(name='weight', verbose_name='Вес',
                                 default=100,
                                 help_text='Целое число x, 0 < x < 32767',
                                 validators=[MinValueValidator(1),
                                             MaxValueValidator(32766)],)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Item(PublishedBaseModel):
    name = models.CharField(name='name', verbose_name='Название товара',
                            max_length=150,
                            help_text='Максимум 150 символов',
                            default='')
    text = models.TextField(name='text', verbose_name='Описание',
                            default='',
                            validators=[validate_perfect],
                            help_text=('Обязательно используйте слово роскошно'
                                       ' или превосходно!'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='items',
                                 verbose_name='Категория')
    tags = models.ManyToManyField(Tag, related_name='items',
                                  verbose_name='Тэги')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
