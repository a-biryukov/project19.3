from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (CategoryListView, ProductListView, ProductDetailView, ContactsTemplateView,
                           ProductCreateView, ProductUpdateView, ProductDeleteView, UserProductList)

app_name = CatalogConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='category_list'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<int:category_id>/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('product/user-product', UserProductList.as_view(), name='user_product_list')
]
