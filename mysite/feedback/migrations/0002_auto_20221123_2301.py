# Generated by Django 3.2.4 on 2022-11-23 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'отзыв', 'verbose_name_plural': 'отзывы'},
        ),
        migrations.AddField(
            model_name='feedback',
            name='mail',
            field=models.EmailField(default='404@example.com', max_length=254, verbose_name='почта'),
        ),
    ]
