from django.db import models
from sorl.thumbnail import get_thumbnail


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField('опубликовано', name='is_published',
                                       default=True)

    class Meta:
        abstract = True


class SlugBaseModel(models.Model):
    slug = models.SlugField('идентификатор (slug)', max_length=200,
                            unique=True)

    class Meta:
        abstract = True


class ImageBaseModel(models.Model):
    image = models.ImageField('изображение', upload_to='media/%Y/%m',
                              default='')

    @property
    def get_img(self):
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)
