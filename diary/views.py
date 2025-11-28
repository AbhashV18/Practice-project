from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Lesson, Grade


@login_required
def schedule_view(request):
    try:
        current_day = int(request.GET.get("day", -1))
    except ValueError:
        current_day = -1

    if current_day not in range(0, 7):
        current_day = 0

    lessons = Lesson.objects.filter(weekday=current_day).order_by("start_time")

    context = {
        "current_day": current_day,
        "lessons": lessons,
        "weekdays": Lesson.WEEKDAYS,
    }
    return render(request, "diary/schedule.html", context)


@login_required
def grades_view(request):
    grades = Grade.objects.filter(student=request.user).select_related("subject")

    subjects = {}
    for grade in grades:
        subjects.setdefault(grade.subject, []).append(grade)

    context = {
        "subjects": subjects
    }
    return render(request, "diary/grades.html", context)
