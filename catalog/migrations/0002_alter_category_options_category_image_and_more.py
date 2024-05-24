# Generated by Django 5.0.6 on 2024-05-23 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите изображение продукта', null=True, upload_to='product/images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(help_text='Выберите категорию', on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, help_text='Введите дату записи в БД', verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(auto_now=True, help_text='Введите дату последнего изменения', verbose_name='Дата изменения'),
        ),
    ]
