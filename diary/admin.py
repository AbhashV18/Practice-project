from django.contrib import admin

from .models import Subject, Lesson, Grade

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "grade_type", "grade_value", "date")
    list_filter = ("subject", "grade_type", "grade_value")
    search_fields = ("student__username", "subject__name", "comment")
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
