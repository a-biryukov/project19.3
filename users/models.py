import secrets

from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django_countries.fields import CountryField
from django.db import models

from config.settings import EMAIL_HOST_USER, NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    avatar = models.ImageField(upload_to="users/avatars", verbose_name="Аватар", **NULLABLE, help_text="Загрузите фото")
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE, help_text="Введите номер телефона")
    country = CountryField(verbose_name="Страна", help_text="Выберите страну", **NULLABLE)
    token = models.CharField(max_length=100, verbose_name="Токен", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email

    def email_send(self, subject, message):
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[self.email]
        )

    def make_token(self):
        self.token = secrets.token_hex(16)

    def set_password(self, raw_password=None):
        if raw_password:
            super().set_password(raw_password)
        else:
            raw_password = User.objects.make_random_password()
            super().set_password(raw_password)
            return raw_password
