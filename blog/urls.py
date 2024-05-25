from blog.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView
from blog.apps import BlogConfig
from django.urls import path

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('blogs/create/', BlogCreateView.as_view(), name='blog_form'),
    path('blog/view/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_detail')
]
