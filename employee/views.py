from django.db.models import Count, Q
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)

from employee.models import Employee
from employee.serializers import EmployeeSerializer, EmployeeTaskSerializer


class EmployeeCreateAPIView(CreateAPIView):
    """Создание работника."""

    serializer_class = EmployeeSerializer


class EmployeeListAPIView(ListAPIView):
    """Просмотр листа работников."""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeRetrieveAPIView(RetrieveAPIView):
    """Просмотр работника."""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeUpdateAPIView(UpdateAPIView):
    """Редактирование работника."""

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


class EmployeeDestroyAPIView(DestroyAPIView):
    """Удаление работника."""

    queryset = Employee.objects.all()


class EmployeeTaskListAPIView(ListAPIView):
    """Просмотр для подсчета активных задач работника."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeTaskSerializer

    def get_queryset(self):
        return (
            Employee.objects.annotate(
                active_tasks_count=Count("tasks", filter=Q(tasks__status="start"))
            )
            .filter(active_tasks_count__gt=0)
            .order_by("-active_tasks_count")
        )