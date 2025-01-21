from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"null": True, "blank": True}


class User(AbstractUser):
    """Создаем модель юзера."""

    username = None
    email = models.EmailField(
        unique=True,
        verbose_name="Email Address",
        max_length=255,
        help_text="Введите почту",
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Phone Number",
        help_text="Введите телефон",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"