from django.contrib import admin
from .models import Subject, Lesson, Grade

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "grade_type", "grade_value", "date")
    list_filter = ("subject", "grade_type", "grade_value")
    search_fields = ("student__username", "subject__name", "comment")
