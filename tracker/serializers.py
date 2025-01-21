from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from employee.models import Employee
from tracker.models import Task
from tracker.validators import NameValidator


class TaskSerializer(ModelSerializer):
    """Сериалайзер модели задачи."""

    class Meta:
        model = Task
        fields = "__all__"
        validators = [
            NameValidator(field="name"),
            UniqueTogetherValidator(fields=["name"], queryset=Task.objects.all()),
        ]


class MainTaskSerializer(ModelSerializer):
    """Сериалайзер для поиска менее загруженных сотрудников."""

    tasks = TaskSerializer(source="other", many=True)
    available_employees = SerializerMethodField()

    class Meta:
        model = Task
        fields = "__all__"

    def get_available_employees(self, task):
        employees = Employee.objects.all()
        emp_data = {}
        for emp in employees:
            list_task = emp.tasks.filter(status="start")
            emp_data[emp.pk] = len(list_task)
        min_count = min(emp_data.values())
        available_employees = [
            emp.full_name for emp in employees if emp_data[emp.pk] == min_count
        ]
        for emp in employees:
            tasks = Task.objects.filter(parent_task=task.id)
            for t in tasks:
                if t.employee == emp and emp.full_name not in available_employees:
                    available_employees.append(emp.full_name)
        return available_employees