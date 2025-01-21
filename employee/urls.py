from django.urls import path

from employee.apps import EmployeeConfig
from employee.views import (EmployeeCreateAPIView, EmployeeDestroyAPIView,
                             EmployeeListAPIView, EmployeeRetrieveAPIView,
                             EmployeeTaskListAPIView, EmployeeUpdateAPIView)

app_name = EmployeeConfig.name

urlpatterns = [
    path("create/", EmployeeCreateAPIView.as_view(), name="employee-create"),
    path("list/", EmployeeListAPIView.as_view(), name="employee-list"),
    path("<int:pk>/", EmployeeRetrieveAPIView.as_view(), name="employee-retrieve"),
    path("update/<int:pk>/", EmployeeUpdateAPIView.as_view(), name="employee-update"),
    path("delete/<int:pk>/", EmployeeDestroyAPIView.as_view(), name="employee-delete"),
    path("employee_task/", EmployeeTaskListAPIView.as_view(), name="employee-task"),
]
