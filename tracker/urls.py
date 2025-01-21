from django.urls import path

from tracker.apps import TrackerConfig
from tracker.views import (TaskCreateAPIView, TaskDestroyAPIView,
                                TaskImportantListAPIView, TaskListAPIView,
                                TaskRetrieveAPIView, TaskUpdateAPIView)

app_name = TrackerConfig.name

urlpatterns = [
    path("create/", TaskCreateAPIView.as_view(), name="task-create"),
    path("list/", TaskListAPIView.as_view(), name="task-list"),
    path("<int:pk>/", TaskRetrieveAPIView.as_view(), name="task-retrieve"),
    path("update/<int:pk>/", TaskUpdateAPIView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDestroyAPIView.as_view(), name="task-delete"),
    path("tracker/", TaskImportantListAPIView.as_view(), name="tracker"),
]