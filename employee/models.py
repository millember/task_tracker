from django.db import models

NULLABLE = {"blank": True, "null": True}


class Employee(models.Model):
    """Создаем модель работника."""

    full_name = models.CharField(
        max_length=100, verbose_name="Full Name", help_text="Введите ФИО"
    )
    post = models.CharField(
        max_length=100, verbose_name="Post", help_text="Введите должность", **NULLABLE
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"