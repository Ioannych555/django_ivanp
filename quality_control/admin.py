from django.contrib import admin
from .models import BugReport, FeatureRequest


@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'task', 'project')
    search_fields = ('title', 'description')


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'priority', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'task', 'project')
    search_fields = ('title', 'description')


@admin.action(description='Поменять статус на "Завершено"')
def change_to_completed(self, request, queryset):
    queryset.update(status='Completed')
    self.message_user(request, f"Изменён статус на 'Завершено'.")


@admin.action(description='Поменять статус на "Новый"')
def change_to_new(self, request, queryset):
    queryset.update(status='New')
    self.message_user(request, f"Изменён статус на 'Новый'")


@admin.action(description='Поменять статус на "В работе"')
def change_to_in_progress(self, request, queryset):
    queryset.update(status='In_progress')
    self.message_user(request, f"Изменён статус на 'В работе'.")
