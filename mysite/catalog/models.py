from core.models import PublishedBaseModel, SlugBaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from .validators import validate_perfect


class Tag(PublishedBaseModel, SlugBaseModel):
    name = models.CharField('название тэга',
                            max_length=150,
                            help_text='Максимум 150 символов',
                            default='Здесь должно быть название', unique=True)

    class Meta:
        verbose_name = 'тэг'
        verbose_name_plural = 'тэги'
        default_related_name = 'tags'

    def __str__(self):
        return self.name


class Category(PublishedBaseModel, SlugBaseModel):
    name = models.CharField('название категории',
                            max_length=150,
                            help_text='Максимум 150 символов',
                            default='Здесь должно быть название', unique=True)
    weight = models.SmallIntegerField('вес',
                                      default=100,
                                      help_text='Целое число x, 0 < x < 32767',
                                      validators=[MinValueValidator(1),
                                                  MaxValueValidator(32766)])

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Item(PublishedBaseModel):
    name = models.CharField('название товара',
                            max_length=150,
                            help_text='Максимум 150 символов',
                            default='Здесь должно быть название')
    text = models.TextField(verbose_name='Описание',
                            default='',
                            validators=[validate_perfect('роскошно',
                                                         'превосходно')],
                            help_text=('Обязательно используйте слово роскошно'
                                       ' или превосходно!'))
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='категория')
    tags = models.ManyToManyField(Tag,
                                  verbose_name='тэги')

    image = models.ImageField('изображение', upload_to='media/%Y/%m',
                              default='')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        default_related_name = 'items'

    def __str__(self):
        return self.name

    @property
    def get_img(self):
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'превью'
    image_tmb.allow_tags = True


class Gallery(models.Model):
    image = models.ImageField(upload_to='media/%Y/%m',
                              default='')
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             verbose_name='товар')

    @property
    def get_img(self):
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'фотогалерея'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'фотогалерея'
        verbose_name_plural = 'фото из галереи'
        default_related_name = 'gallery'
