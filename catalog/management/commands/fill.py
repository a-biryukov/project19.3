import json

from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('fixtures/category_data.json', encoding='utf-16') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
        with open('fixtures/product_data.json', encoding='utf-16') as file:
            return json.load(file)

    def handle(self, *args, **options):

        # Удаление старых данных
        Product.objects.all().delete()
        Category.truncate_table_restart_id()

        # Списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Создаем объекты категорий из фикстур
        for category in Command.json_read_categories():
            category_data = category.get('fields')
            category_for_create.append(
                Category(**category_data)
            )

        # Создаем объекты категорий в базе
        Category.objects.bulk_create(category_for_create)

        # Создаем объекты продуктов из фикстур
        for product in Command.json_read_products():
            product_data = product.get('fields')
            product_for_create.append(
                Product(
                    name=product_data.get('name'),
                    description=product_data.get('description'),
                    image=product_data.get('image'),
                    category=Category.objects.get(pk=product_data.get('category')),
                    price=product_data.get('price'),
                    created_at=product_data.get('created_at'),
                    updated_at=product_data.get('updated_at'))
            )

        # Создаем объекты продуктов в базе
        Product.objects.bulk_create(product_for_create)
