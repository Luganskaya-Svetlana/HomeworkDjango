from core.models import ImageBaseModel, PublishedBaseModel, SlugBaseModel
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.query import Prefetch
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


class ItemManager(models.Manager):
    def published(self):
        return (
            self.get_queryset()
                .filter(is_published=True, category__is_published=True)
                .select_related('category')
                .prefetch_related(Prefetch
                                  ('tags',
                                   queryset=Tag.objects
                                               .all()
                                               .filter(is_published=True)))
                .only('name', 'text', 'category__name')
        )


class Item(PublishedBaseModel):
    objects = ItemManager()
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

    is_on_main = models.BooleanField('показывать на главной', default=False)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        default_related_name = 'items'

    def __str__(self):
        return self.name

    def main_image_tmb(self):
        if self.main_image:
            return mark_safe(
                f'<img src="{self.main_image.get_small_img.url}">'
            )
        return 'Нет изображения'

    main_image_tmb.short_description = 'превью'
    main_image_tmb.allow_tags = True


class GalleryImage(ImageBaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             verbose_name='товар', null=True)

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'изображение для галереи'
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = 'изображение для галереи'
        verbose_name_plural = 'изображения для галереи'
        default_related_name = 'gallery'

    def __str__(self):
        return f'Одно из изображений для {self.item}'


class MainImage(ImageBaseModel):
    item = models.OneToOneField(Item, on_delete=models.CASCADE,
                                verbose_name='товар', null=True)

    class Meta:
        verbose_name = 'главное изображение'
        verbose_name_plural = 'главные изображения'
        default_related_name = 'main_image'

    @property
    def get_small_img(self):
        return get_thumbnail(self.image, '50x50', crop='center', quality=51)

    def image_tmb_small(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_small_img.url}">'
            )
        return 'Нет изображения'

    image_tmb_small.short_description = 'превью'
    image_tmb_small.allow_tags = True

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'Нет изображения'

    image_tmb.short_description = 'главное фото'
    image_tmb.allow_tags = True

    def __str__(self):
        return f'Главное изображение для {self.item}'
