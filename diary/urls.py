from django.urls import path
from .views import schedule_view, grades_view

urlpatterns = [
    path('schedule/', schedule_view, name='schedule'),
    path('grades/', grades_view, name='grades'),
]
from django.urls import path
from .views import homework_view

urlpatterns += [
    path('homework/', homework_view, name='homework'),
]
