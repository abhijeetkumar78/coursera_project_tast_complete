from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'course', 'enrollment_date', 'created_at')
    list_filter = ('course', 'enrollment_date')
    search_fields = ('first_name', 'last_name', 'email', 'course')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
