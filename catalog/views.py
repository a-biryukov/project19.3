from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def contacts(request):
    return render(request, 'contacts.html')


def user_info(request):
    print(1)
    if request.method == 'POST':
        print(2)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)
    return render(request, 'contacts.html')
