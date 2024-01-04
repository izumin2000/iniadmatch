from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import generic
from .models import *
import re
import datetime

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
    def get(self, request, *args, **kwargs):
        d = {}
        teacher = request.user
        d["viewname"] = teacher.account.name
        for week in range(5) :
            teacher_routine = Routine.objects.filter(teacher__account__user=teacher, week=week)
            if teacher_routine :
                teacher_routine = teacher_routine.first()
                d[f'week{week}_start'], d[f'week{week}_end'] = teacher_routine.start, teacher_routine.end
            else :
                d[f'week{week}_start'], d[f'week{week}_end'] = "", ""
                
        return render(request, self.template_name, d)
        
    def post(self, request, *args, **kwargs):
        d = {}
        
        post = request.POST
        viewname = post.get('viewname', '')
        d["viewname"] = viewname
        
        teacher = request.user
        account_rec = Account.objects.filter(user=teacher).first()
        account_rec.name = viewname
        account_rec.save()
        for week in range(5) :
            start, end = post.get(f'week{week}_start', ''), post.get(f'week{week}_end', '')
            teacher_routine = Routine.objects.filter(teacher__account__user=teacher, week=week)
            if ("" in [start, end]) :
                if teacher_routine :
                    teacher_routine.delete()
                
            else :
                teacher_routine, _ = Routine.objects.get_or_create(teacher__account__user=teacher, week=week)
                teacher_routine.teacher = teacher.account.teacher
                teacher_routine.start = datetime.datetime.strptime(start, "%H:%M").time()
                teacher_routine.end = datetime.datetime.strptime(end, "%H:%M").time()
                teacher_routine.save()
                d[f'week{week}_start'], d[f'week{week}_end'] = start, end
                
        return render(request, self.template_name, d)
    
    
class CustomLoginView(LoginView) :
    template_name = 'iniadmatch/top.html'
    
    def get_success_url(self):
        print(f"\033[31m{0}\033[0m")
        Account.objects.get_or_create(user=self.request.user, defaults={"name": self.request.user})
        return super().get_success_url()


class CustomLogoutView(LogoutView) :
    template_name = 'iniadmatch/top.html'