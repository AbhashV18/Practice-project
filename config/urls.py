from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from accounts.views import CustomLoginView, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),

    # логін з кастомним редіректом
    path('login/', CustomLoginView.as_view(), name='login'),

    # вихід
    path('logout/', user_logout, name='logout'),

    # корінь сайту → одразу на розклад
    path('', lambda request: redirect('schedule'), name='home'),

    # розклад, оцінки, домашка
    path('', include('diary.urls')),
]
