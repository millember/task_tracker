from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Тесты для модели user."""

    def setUp(self):
        """Предварительная настройка."""
        self.user = User.objects.create(email="test@example.com")
        self.user.set_password("test")
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """Тест на создание модели."""

        url = reverse("users:user-register")
        data = {"email": "user@example.com", "password": "1password1"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)

    def test_get_token(self):
        """Тест на получение токена."""

        url = reverse("users:token_obtain_pair")
        data = {"email": "test@example.com", "password": "test"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(bool(response.json().get("access")), True)