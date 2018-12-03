from django.contrib.auth.views import LoginView, LogoutView


class Login(LoginView):
    template_name = 'loginsys/login.html'


class Logout(LogoutView):
    next_page = '/'
