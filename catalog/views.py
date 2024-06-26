from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductModeratorForm
from catalog.models import Product, Category, Version
from catalog.services import get_categories_from_cache, add_version_info


class CategoryListView(ListView):
    model = Category

    def get_queryset(self):
        return get_categories_from_cache()


class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(category=self.kwargs.get("category_id"))
        if not user.groups.filter(name="Модератор").exists() and user.is_superuser is not True:
            queryset = queryset.filter(is_published=True)
        queryset = add_version_info(queryset)
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_list', args=[self.object.category_id])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == "POST":
            context_data["formset"] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data["formset"] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data["formset"]
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))

    def get_form_class(self):
        user = self.request.user
        if (
              user.has_perm('catalog.can_edit_publication') and
              user.has_perm('catalog.can_edit_description') and
              user.has_perm('catalog.can_edit_category')
        ):
            return ProductModeratorForm
        elif user == self.object.owner:
            return ProductForm
        raise PermissionDenied


class ProductDeleteView(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse('catalog:product_list', args=[self.object.category_id])


class UserProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog/user_product_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        user = self.request.user.id
        queryset = queryset.filter(owner=user)
        queryset = add_version_info(queryset)
        return queryset


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
        return super().get(request, *args, **kwargs)
