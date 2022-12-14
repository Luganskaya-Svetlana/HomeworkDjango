# Generated by Django 3.2 on 2022-11-02 11:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20221102_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='weight',
            field=models.SmallIntegerField(default=100, help_text='Целое число x, 0 < x < 32767', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(32766)], verbose_name='вес'),
        ),
    ]
