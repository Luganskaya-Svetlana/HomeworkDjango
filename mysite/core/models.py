from django.db import models


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
