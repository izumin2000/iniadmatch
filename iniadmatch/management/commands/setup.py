from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from iniadmatch.models import *
from datetime import time, date
from config.local_settings import SUB_DEV_USER_PASSWORD

class Command(BaseCommand) :
    def handle(self, *args, **options) :
        Account.objects.all().delete()
        Teacher.objects.all().delete()
        Tag.objects.all().delete()
        Routine.objects.all().delete()
        Schedule.objects.all().delete()
        
        teacher1_user = User.objects.get(username = "minecraftiniad")
        teacher2_user = User.objects.get(username = "kanapan2.poo")
        student1_user = User.objects.get(username = "s3f102300023")
        if User.objects.filter(username = "s3f10230024") :
            student2_user = User.objects.create_user(username = "s3f102300024", password=SUB_DEV_USER_PASSWORD)
        
        Account.objects.create(name = "泉川 叶多", user = student1_user).save()
        teacher1_account = Account.objects.create(name = "矢代", user = teacher1_user)
        teacher2_account = Account.objects.create(name = "石川", user = teacher2_user)
        teacher1_account.save()
        teacher2_account.save()
        
        teacher1 = Teacher.objects.create(account = teacher1_account)
        teacher2 = Teacher.objects.create(account = teacher2_account)
        teacher1.save()
        teacher2.save()
        
        tag_1 = Tag.objects.create(name = "CS", teacher = teacher1) 
        tag_2 = Tag.objects.create(name = "研究の相談", teacher = teacher1)
        tag_3 = Tag.objects.create(name = "Django", teacher = teacher2)
        tag_1.save()
        tag_2.save()
        tag_3.save()
        
        routine_1 = Routine.objects.create(teacher = teacher1, week = 0, start = time(13, 0), end = time(14, 30))
        routine_2 = Routine.objects.create(teacher = teacher1, week = 2, start = time(14, 45), end = time(16, 15))
        routine_3 = Routine.objects.create(teacher = teacher2, week = 2, start = time(14, 45), end = time(16, 15))
        routine_1.save()        
        routine_2.save()        
        routine_3.save()        

        Schedule.objects.create(routine=routine_1, date=date(2024, 1, 17)).save()
        Schedule.objects.create(routine=routine_2, date=date(2024, 1, 18)).save()
        Schedule.objects.create(routine=routine_2, date=date(2024, 1, 18)).save()
        Schedule.objects.create(routine=routine_3, date=date(2024, 1, 16)).save()
        