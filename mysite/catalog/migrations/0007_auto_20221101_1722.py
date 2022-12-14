# Generated by Django 3.2 on 2022-11-01 14:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20221030_1935'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'default_related_name': 'items', 'verbose_name': 'товар', 'verbose_name_plural': 'товары'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'тэг', 'verbose_name_plural': 'тэги'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Здесь должно быть название', help_text='Максимум 150 символов', max_length=150, unique=True, verbose_name='название категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='Идентификатор (slug)'),
        ),
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.IntegerField(default=100, help_text='Целое число x, 0 < x < 32767', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(32766)], verbose_name='вес'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='catalog.category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(default='Здесь должно быть название', help_text='Максимум 150 символов', max_length=150, verbose_name='название товара'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tags',
            field=models.ManyToManyField(related_name='items', to='catalog.Tag', verbose_name='тэги'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default='Здесь должно быть название', help_text='Максимум 150 символов', max_length=150, unique=True, verbose_name='название тэга'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), 'Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.', 'invalid')], verbose_name='Идентификатор (slug)'),
        ),
    ]
