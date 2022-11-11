from core.models import ImagesBaseModel, PublishedBaseModel, SlugBaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from .validators import validate_perfect


class MainImage(ImagesBaseModel):
    class Meta:
        verbose_name = 'главное изображение'
        verbose_name_plural = 'главные изображения'
        default_related_name = 'image'

    @property
    def get_small_img(self):
        return get_thumbnail(self.image, '50x50', crop='center', quality=51)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'главное фото'
    image_tmb.allow_tags = True

    def image_tmb_small(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_small_img.url}">'
            )
        return 'Нет изображения'

    image_tmb_small.short_description = 'превью'
    image_tmb_small.allow_tags = True

    def __str__(self):
        return f'Главное изображение для {self.item}'


class GalleryImage(ImagesBaseModel):
    class Meta:
        verbose_name = 'фото для галереи'
        verbose_name_plural = 'фото для галереи'
        default_related_name = 'gallery'

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'фото для галереи'
    image_tmb.allow_tags = True

    def __str__(self):
        return f'Одно из фото для {self.item}'


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
    image = models.OneToOneField(MainImage, on_delete=models.CASCADE,
                                 verbose_name='главное изображение')
    gallery = models.ManyToManyField(GalleryImage,
                                     verbose_name='изображение из галереи')

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        default_related_name = 'items'

    def __str__(self):
        return self.name
