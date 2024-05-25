import json

from django.core.management import BaseCommand
from blog.models import Blog


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('fixtures/blog_data.json', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):

        # Удаление старых данных
        Blog.truncate_table_restart_id()

        # Списки для хранения объектов
        blog_for_create = []

        # Создаем объекты отзывов из фикстур
        for blog in Command.json_read_categories():
            category_data = blog.get('fields')
            blog_for_create.append(
                Blog(**category_data)
            )

        # Создаем объекты категорий в базе
        Blog.objects.bulk_create(blog_for_create)
