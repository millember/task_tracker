from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from employee.models import Employee
from tracker.models import Task


class TaskTestCase(APITestCase):
    """Тесты для модели задачи."""

    def setUp(self):
        """Предварительная настройка."""
        self.task = Task.objects.create(
            name="Тест задача",
            parent_task=None,
            employee=None,
            deadline="2024-09-12",
            status="start",
        )

    def test_task_create(self):
        """Тест на создание модели."""
        url = reverse("task_tracker:task-create")
        data = {
            "name": "Написать программу",
            "parent_task": None,
            "employee": None,
            "deadline": "2024-12-12",
            "status": "start",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Написать программу")
        self.assertEqual(response.data["parent_task"], None)
        self.assertEqual(response.data["employee"], None)
        self.assertEqual(response.data["deadline"], "2024-12-12")
        self.assertEqual(response.data["status"], "start")
        self.assertEqual(Task.objects.count(), 2)

    def test_task_retrieve(self):
        """Тест на просмотр модели."""
        url = reverse("task_tracker:task-retrieve", args=(self.task.id,))
        response = self.client.get(url, format="json")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data["name"], self.task.name)
        self.assertEqual(data["parent_task"], self.task.parent_task)
        self.assertEqual(data["employee"], self.task.employee)
        self.assertEqual(data["deadline"], self.task.deadline)
        self.assertEqual(data["status"], self.task.status)

    def test_task_update(self):
        """Тест на редактор модели."""
        url = reverse("task_tracker:task-update", args=(self.task.id,))
        response = self.client.patch(url, {"name": "update task"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "update task")

    def test_task_delete(self):
        """Тест на удаление модели."""
        url = reverse("task_tracker:task-delete", args=(self.task.id,))
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_task_list(self):
        """Тест на просмотр листа моделей."""
        url = reverse("task_tracker:task-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)

    def test_important_task_list(self):
        """Тест поиск менее загруженных сотрудников."""
        employee = Employee.objects.create(full_name="Тест работник", post="Тест пост")
        Task.objects.create(
            name="Тест задача",
            employee=employee,
            deadline=None,
            status="start",
            parent_task=self.task,
        )
        url = reverse("task_tracker:tracker")
        response = self.client.get(url, format="json")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data[0]["available_employees"], ["Тест работник"])