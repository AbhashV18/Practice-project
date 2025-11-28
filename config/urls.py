from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts.views import user_logout
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login.html'
    ), name='login'),

    path('logout/', user_logout, name='logout'),

    path('accounts/', include('accounts.urls')),

    # Усі сторінки щоденника (розклад, оцінки і т.д.)
    path('', include('diary.urls')),
]
