from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import generic
from .models import *

class TopView(generic.ListView) :
    template_name = 'iniadmatch/top.html'
    model = Schedule

    def get(self, request, *args, **kwargs) :
        if not request.user.is_authenticated :
            return redirect('login')

        return render(request, self.template_name)


class ScheduleView(generic.DetailView) :
    template_name = 'iniadmatch/schedule.html'
    model = Schedule

    
class SearchView(generic.TemplateView) :
    template_name = 'iniadmatch/search.html'


class SettingView(generic.TemplateView) :
    template_name = 'iniadmatch/setting.html'


class CustomLoginView(LoginView) :
    template_name = 'iniadmatch/top.html'


class CustomLogoutView(LogoutView) :
    template_name = 'iniadmatch/top.html'