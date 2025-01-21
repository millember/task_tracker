from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Employee
from tracker.models import Task


class EmployeeTestCase(APITestCase):
    """Тесты для модели работника."""

    def setUp(self):
        """Предварительная настройка."""
        self.employee = Employee.objects.create(
            full_name="Тест имя", post="Тест должность"
        )

    def test_employee_create(self):
        """Тест на создание модели."""
        url = reverse("employees:employee-create")
        data = {"full_name": "Гладков Сергей", "post": "developer"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["full_name"], "Гладков Сергей")
        self.assertEqual(response.data["post"], "developer")
        self.assertEqual(Employee.objects.count(), 2)

    def test_employee_retrieve(self):
        """Тест на просмотр модели."""
        url = reverse("employees:employee-retrieve", args=(self.employee.id,))
        response = self.client.get(url, format="json")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["full_name"], self.employee.full_name)
        self.assertEqual(data["post"], self.employee.post)

    def test_employee_update(self):
        """Тест на редактор модели."""
        url = reverse("employees:employee-update", args=(self.employee.id,))
        response = self.client.patch(
            url, data={"full_name": "updated name", "post": "update developer"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["full_name"], "updated name")
        self.assertEqual(response.data["post"], "update developer")

    def test_employee_delete(self):
        """Тест на удаление модели."""
        url = reverse("employees:employee-delete", args=(self.employee.id,))
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)

    def test_employee_list(self):
        """Тест на просмотр листа моделей."""
        url = reverse("employees:employee-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Employee.objects.count(), 1)

    def test_employee_task_list(self):
        """Тест для подсчета активных задач работника"""
        Task.objects.create(
            name="Test task",
            employee=self.employee,
            deadline=None,
            status="start",
            parent_task=None,
        )
        url = reverse("employees:employee-task")
        response = self.client.get(url, format="json")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0]["active_tasks_count"], 1)