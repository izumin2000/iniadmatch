from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View


class TopView(View):
    template_name = 'iniadmatch/top.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        return render(request, self.template_name)


class CustomLoginView(LoginView):
    template_name = 'iniadmatch/top.html'


class CustomLogoutView(LogoutView):
    template_name = 'iniadmatch/top.html'