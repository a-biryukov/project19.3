from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
from django.db import models


NULLABLE = {"blank": True, "null": True}


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

