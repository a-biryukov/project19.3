from django.shortcuts import render

from catalog.models import Product


def index(request):
    return render(request, 'categories_menu.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'contacts.html')


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)


def products_list(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    context = {'products': products}
    return render(request, 'products_list.html', context)
