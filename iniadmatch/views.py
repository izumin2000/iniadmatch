from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import generic
from .models import *
import re

def isTeacher(user):
    return not bool(re.match(r'^s\df\d{9}$', user.username))

class TopView(generic.ListView):
    template_name = 'iniadmatch/top.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        is_teacher = isTeacher(request.user)
        if is_teacher:
            teacher = request.user
            all_schedules = Schedule.objects.filter(teacher__account__user=teacher)
            return render(request, self.template_name, {'is_teacher': is_teacher, 'schedules': all_schedules})
        else:
            all_schedules = Schedule.objects.all()
            return render(request, self.template_name, {'is_teacher': is_teacher, 'schedules': all_schedules})



class ScheduleView(generic.DetailView) :
    template_name = 'iniadmatch/schedule.html'
    model = Schedule

    
class SearchView(generic.TemplateView) :
    template_name = 'iniadmatch/search.html'


class SettingView(generic.TemplateView) :
    template_name = 'iniadmatch/setting.html'


class CustomLoginView(LoginView) :
    template_name = 'iniadmatch/top.html'
    
    def get_success_url(self):
        print(f"\033[31m{0}\033[0m")
        Account.objects.get_or_create(user=self.request.user, defaults={"name": self.request.user})
        return super().get_success_url()


class CustomLogoutView(LogoutView) :
    template_name = 'iniadmatch/top.html'