from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from iniadmatch.models import *
from datetime import time, datetime
from config.local_settings import SUB_DEV_USER_PASSWORD
from django.utils import timezone

class Command(BaseCommand) :
    def handle(self, *args, **options) :
        Account.objects.all().delete()
        Teacher.objects.all().delete()
        Tag.objects.all().delete()
        Routine.objects.all().delete()
        
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
        tag_1.save()
        tag_2.save()
        
        teacher1 = Teacher.objects.get(account=teacher1_account)
        
        Routine.objects.create(teacher = teacher1, week = 0, start = time(13, 0), end = time(14, 30)).save()
        Routine.objects.create(teacher = teacher1, week = 2, start = time(14, 45), end = time(16, 15)).save()
        

        utc_timezone = timezone.utc
        start_datetime1 = datetime(2024, 1, 15, 13, 0, tzinfo=utc_timezone)
        end_datetime1 = datetime(2024, 1, 15, 14, 30, tzinfo=utc_timezone)
        Schedule.objects.create(teacher=teacher1, start=start_datetime1, end=end_datetime1).save()

        start_datetime2 = datetime(2024, 1, 17, 14, 45, tzinfo=utc_timezone)
        end_datetime2 = datetime(2024, 1, 17, 16, 15, tzinfo=utc_timezone)
        Schedule.objects.create(teacher=teacher1, start=start_datetime2, end=end_datetime2).save()

        start_datetime3 = datetime(2024, 1, 16, 14, 45, tzinfo=utc_timezone)
        end_datetime3 = datetime(2024, 1, 16, 16, 15, tzinfo=utc_timezone)
        Schedule.objects.create(teacher=teacher2, start=start_datetime3, end=end_datetime3).save()
        