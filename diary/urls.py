from django.urls import path

from .views import schedule_view, grades_view

urlpatterns = [
    path('schedule/', schedule_view, name='schedule'),
    path('grades/', grades_view, name='grades'),

from .views import schedule_view

urlpatterns = [
    path('', schedule_view, name='schedule'),

]