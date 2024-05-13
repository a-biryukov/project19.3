from django.db import models, connection


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Наименование',help_text='Введите название категории'
    )
    description = models.TextField(
        verbose_name='Описание', help_text='Введите описание категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['name']

    def __str__(self):
        return self.name

    @staticmethod
    def truncate_table_restart_id():
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE catalog_category * RESTART IDENTITY CASCADE')


class Product(models.Model):
    name = models.CharField(
        max_length=100, verbose_name='Наименование', help_text='Введите название товара'
    )
    description = models.TextField(
        verbose_name='Описание', help_text='Введите описание товара'
    )
    image = models.ImageField(
        upload_to='product/image', blank=True, null=True,
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

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'category', 'price', 'created_at', 'updated_at']

    def __str__(self):
        return self.name

