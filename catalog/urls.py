from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, user_info

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('contacts/', user_info, name='contacts')
]
