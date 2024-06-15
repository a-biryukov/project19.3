from django.db import models, connection
from users.models import NULLABLE


class Blog(models.Model):
    tittle = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='blog/images', **NULLABLE, verbose_name='Изображение')
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)

    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name=' Просмотры')
    slug = models.CharField(max_length=100, verbose_name='Slug', **NULLABLE)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    @staticmethod
    def truncate_table_restart_id():
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE blog_blog * RESTART IDENTITY')
