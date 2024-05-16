from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, products_list, product_detail, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('category/<int:category_id>', products_list, name='products_list')
]
