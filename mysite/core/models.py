from django.db import models
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail


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

    class Meta:
        abstract = True

    @property
    def get_img(self):
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)
