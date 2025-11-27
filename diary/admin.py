from django.contrib import admin
from .models import Subject, Lesson


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "short_name")
    search_fields = ("name", "short_name")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("subject", "weekday", "start_time", "end_time", "room", "teacher", "lesson_type")
    list_filter = ("weekday", "lesson_type", "subject")
    search_fields = ("subject__name", "teacher", "room")
