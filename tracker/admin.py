from django.contrib import admin

from tracker.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "deadline", "status")