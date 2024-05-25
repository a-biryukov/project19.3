from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from blog.models import Blog


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("tittle", "text", "image")
    success_url = reverse_lazy("blog:blog_list")


class BlogDetailView(DetailView):
    model = Blog
