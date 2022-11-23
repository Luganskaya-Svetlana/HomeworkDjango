from django.db import models


class Feedback(models.Model):
    text = models.TextField('текст', help_text='введите свое сообщение')
    mail = models.EmailField('почта', default='404@example.com')
    created_on = models.DateTimeField('время создания', auto_now_add=True)

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
