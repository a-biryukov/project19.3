# Generated by Django 5.0.6 on 2024-06-21 15:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(blank=True, help_text='Введите автора', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите изображение', null=True, upload_to='blog/images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(help_text='Введите текст', verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tittle',
            field=models.CharField(help_text='Введите заголовок', max_length=100, verbose_name='Заголовок'),
        ),
    ]
