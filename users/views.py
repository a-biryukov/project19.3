from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, UpdateView


from users.forms import UserRegisterForm, RecoveryForm, UserUpdateForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        user.make_token()
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{user.token}/'
        user.email_send(subject="Подтверждение почты", message=f"Перейдите по ссылке для подтверждения почты {url}")
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
            print(1)
        else:
            password = user.set_password()
            user.save()
            user.email_send(subject="Восстановление пароля", message=f"Ваш новый пароль: {password}")
        finally:
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["form"] = self.form_class
        return context_data


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))
