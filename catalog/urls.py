from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import CategoryListView, ProductListView, ProductDetailView, ContactsTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:category_id>/', ProductListView.as_view(), name='product_list')
]
