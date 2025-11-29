from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    """
    Користувачі заходять через /login/:
    - якщо це адмін або staff → редірект у /admin/
    - якщо звичайний студент → редірект на розклад
    """
    template_name = 'accounts/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            # адмін іде в адмінку
            return reverse_lazy('admin:index')
        # студент іде на розклад
        return reverse_lazy('schedule')


def user_logout(request):
    logout(request)
    return redirect('login')
