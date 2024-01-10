from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from iniadmatch.models import *
from config.local_settings import SUB_DEV_USER_PASSWORD
from django.db import connection


class Command(BaseCommand) :
    def handle(self, *args, **options) :
        Account.objects.all().delete()
        Teacher.objects.all().delete()
        Tag.objects.all().delete()
        Routine.objects.all().delete()
        Schedule.objects.all().delete()
        
        cursor = connection.cursor()
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='iniadmatch_account'")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='iniadmatch_teacher'")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='iniadmatch_tag'")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='iniadmatch_routine'")
        cursor.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='iniadmatch_schedule'")
        
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