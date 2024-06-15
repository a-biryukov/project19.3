from django.db import models, connection

from users.models import User, NULLABLE


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Наименование', help_text='Введите название категории'
    )
    description = models.TextField(
        verbose_name='Описание', help_text='Введите описание категории'
    )
    image = models.ImageField(
        upload_to='category/images', **NULLABLE,
        verbose_name='Изображение', help_text='Загрузите изображение продукта'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name

    @staticmethod
    def truncate_table_restart_id():
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE catalog_category * RESTART IDENTITY CASCADE')


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Наименование', help_text='Введите название товара'
    )
    description = models.TextField(
        verbose_name='Описание', help_text='Введите описание товара'
    )
    image = models.ImageField(
        upload_to='product/images', **NULLABLE,
        verbose_name='Изображение', help_text='Загрузите изображение продукта'
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Название категории', help_text='Выберите категорию'
    )
    price = models.IntegerField(
        verbose_name='Цена', help_text='Введите цену товара'
    )
    created_at = models.DateField(
        verbose_name='Дата создания', help_text='Введите дату записи в БД', auto_now_add=True
    )
    updated_at = models.DateField(
        verbose_name='Дата изменения', help_text='Введите дату последнего изменения', auto_now=True
    )

    owner = models.ForeignKey(
        User, verbose_name="Владелец", help_text="Введите владельца", **NULLABLE, on_delete=models.SET_NULL
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'price', 'created_at', 'updated_at']

    def __str__(self):
        return self.name


class Version(models.Model):
    product = models.ForeignKey(Product, related_name="Products", on_delete=models.CASCADE, verbose_name="Наименование")
    version_num = models.IntegerField(default=0, verbose_name='Номер версии')
    version_name = models.CharField(max_length=150, verbose_name='Название версии')
    current_version = models.BooleanField(default=True, verbose_name='Текущая версия')

    def __str__(self):
        return self.version_name

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
