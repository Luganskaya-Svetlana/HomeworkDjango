from Core.models import PublishedBaseModel, SlugBaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .validators import validate_perfect


class Tag(PublishedBaseModel, SlugBaseModel):
    name = models.CharField(name='Название тэга', max_length=150,
                            help_text='Максимум 150 символов',
                            default='Названия нет')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Category(PublishedBaseModel, SlugBaseModel):
    name = models.CharField(name='Название', max_length=150,
                            help_text='Максимум 150 символов',
                            default='Названия нет')
    weight = models.IntegerField(name='Вес', default=100,
                                 validators=[MinValueValidator(1),
                                             MaxValueValidator(32766)])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Item(PublishedBaseModel):
    name = models.CharField(name='Название товара', max_length=150,
                            help_text='Максимум 150 символов',
                            default='Названия нет')
    text = models.TextField(name='Описание', validators=[validate_perfect])
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='items', default=None)
    tags = models.ManyToManyField(Tag, related_name='items')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.text[:15]
