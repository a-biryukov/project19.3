from django.core.cache import cache

from catalog.models import Category
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


