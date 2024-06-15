import secrets
import string
from random import choice

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, RecoveryForm, UserUpdateForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        print(self.form_class)
        print(form)
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f"Перейдите по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("catalog:category_list")
    template_name = "users/user_form.html"


class RecoveryTemplateView(TemplateView):
    template_name = 'users/password_recovery.html'
    form_class = RecoveryForm
    success_url = reverse_lazy("users:login")

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print()
        else:
            password = "".join([choice(string.ascii_letters + string.digits) for i in range(10)])
            hash_password = make_password(password)
            user.password = hash_password
            user.save()
            send_mail(
                subject="Восстановление пароля",
                message=f"Ваш новый пароль: {password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
        finally:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["form"] = self.form_class
        return context_data


def email_verification(token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


