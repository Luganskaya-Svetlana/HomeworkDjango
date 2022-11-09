# Generated by Django 3.2 on 2022-11-09 20:55

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20221109_2349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'default_related_name': 'gallery', 'verbose_name': 'фото для галереи', 'verbose_name_plural': 'фото для галереи'},
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='', upload_to='media/%Y/%m', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default='', help_text='Обязательно используйте слово роскошно или превосходно!', validators=[catalog.validators.validate_perfect], verbose_name='Описание'),
        ),
    ]
