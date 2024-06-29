from django.core.cache import cache

from catalog.models import Category, Version
from config.settings import CACHES_ENABLED


def get_categories_from_cache():
    """Получает данные по категориям из кэша, если кэш пуст - получает данные из БД"""
    if not CACHES_ENABLED:
        return Category.objects.all()
    key = 'category_list'
    categories = cache.get(key)
    if categories is not None:
        return categories
    categories = Category.objects.all()
    cache.set(key, categories)
    return categories


def add_version_info(queryset):
    """Добавляет в объкты продуктов информацию о текущей версии"""
    for product in queryset:
        version = Version.objects.filter(product=product)
        current_version = version.filter(current_version=True)
        if current_version:
            product.version_name = current_version.last().version_name
            product.version_num = current_version.last().version_num
    return queryset
