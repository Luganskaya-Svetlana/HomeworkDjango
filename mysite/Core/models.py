from django.core.validators import validate_slug
from django.db import models


class PublishedBaseModel(models.Model):
    is_published = models.BooleanField(name='is_published',
                                       verbose_name='Опубликовано',
                                       default=True)

    class Meta:
        abstract = True


class SlugBaseModel(models.Model):
    slug = models.CharField(name='slug', max_length=200, unique=True,
                            validators=[validate_slug])

    class Meta:
        abstract = True
