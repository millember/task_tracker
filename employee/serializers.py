from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from employee.models import Employee
from tracker.serializers import TaskSerializer


class EmployeeSerializer(ModelSerializer):
    """Сериалайзер модели работника."""

    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeTaskSerializer(TaskSerializer):
    """Сериалайзер модели для подсчета активных задач работника."""

    tasks = TaskSerializer(many=True, read_only=True)
    active_tasks_count = SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            "id",
            "full_name",
            "post",
            "tasks",
            "active_tasks_count",
        )

    def get_active_tasks_count(self, obj):
        return obj.tasks.filter(status="start").count()