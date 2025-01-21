from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from tracker.models import Task
from tracker.serializers import MainTaskSerializer, TaskSerializer


class TaskCreateAPIView(CreateAPIView):
    """Создание задачи."""

    serializer_class = TaskSerializer


class TaskListAPIView(ListAPIView):
    """Просмотр листа задач."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskRetrieveAPIView(RetrieveAPIView):
    """Просмотр задачи."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskUpdateAPIView(UpdateAPIView):
    """Редактирование задачи."""

    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDestroyAPIView(DestroyAPIView):
    """Удаление задачи."""

    queryset = Task.objects.all()


class TaskImportantListAPIView(ListAPIView):
    """Поиск менее загруженных сотрудников."""

    serializer_class = MainTaskSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        return Task.objects.filter(
            other__employee__isnull=False,
            other__status="start",
            employee__isnull=True,
            status="start",
        )