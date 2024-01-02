from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from iniadmatch.models import *
from datetime import time, datetime


class Command(BaseCommand) :
    def handle(self, *args, **options) :
        Account.objects.all().delete()
        Teacher.objects.all().delete()
        Tag.objects.all().delete()
        Routine.objects.all().delete()
        
        student_user = User.objects.get(username = "s3f102300023")
        teacher_user = User.objects.get(username = "minecraftiniad")
        
        Account.objects.create(name = "泉川 叶多", user = student_user).save()
        teacher_account = Account.objects.create(name = "矢代", user = teacher_user)
        teacher_account.save()
        
        teacher = Teacher.objects.create(account = teacher_account)
        teacher.save()
        
        tag_1 = Tag.objects.create(name = "CS", teacher = teacher) 
        tag_2 = Tag.objects.create(name = "研究の相談", teacher = teacher) 
        tag_1.save()
        tag_2.save()
        
        Routine.objects.create(teacher = teacher, week = 0, start = time(13, 0), end = time(14, 30)).save()
        Routine.objects.create(teacher = teacher, week = 2, start = time(14, 45), end = time(16, 15)).save()
        
        Schedule.objects.create(teacher = teacher, start = datetime(2024, 1, 15, 13, 0), end = datetime(2024, 1, 15, 14, 30)).save()
        Schedule.objects.create(teacher = teacher, start = datetime(2024, 1, 17, 14, 45), end = datetime(2024, 1, 17, 16, 15)).save()
        