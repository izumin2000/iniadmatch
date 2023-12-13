from django.db import models
from social_django.models import UserSocialAuth



class Account(models.Model) :
    name = models.CharField(default="", max_length=255, null=True)
    usersocialauth = models.OneToOneField(UserSocialAuth, on_delete=models.CASCADE)

    def get_gmail(self) :
        return self.usersocialauth.uid


class Tag(models.Model) :
    name = models.CharField(default="", max_length=255)


class Teacher(models.Model) :
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def get_name(self) :
        return self.account.name
    
    def get_gmail(self) :
        return self.account.usersocialauth.uid
        

class Schedule(models.Model) :
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    week = models.IntegerField(default=0)
    start = models.TimeField(null=True)
    end = models.TimeField(null=True)

    def get_teacher_name(self) :
        return self.teacher.account.name
    
    def get_week_name(self) :
        week_list = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日"]
        return week_list[self.week]
    

class Booking(models.Model) :
    student = models.ForeignKey(Account, on_delete=models.CASCADE)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE)

    def get_student_name(self) :
        return self.student.name

    def get_teacher_name(self) :
        return self.schedule.teacher.account.name
    
    def get_schedule_data(self) :
        return self.schedule.date
    
    def get_teacher_tags(self) :
        return self.schedule.teacher.tag