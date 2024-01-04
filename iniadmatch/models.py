from django.db import models
from django.contrib.auth.models import User



class Account(models.Model) :
    name = models.CharField(default="", max_length=255, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account", null=True)

    def get_mail(self) :
        return self.user.email


class Teacher(models.Model) :
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="teacher", null=True)

    def get_name(self) :
        return self.account.name
    
    def get_mail(self) :
        return self.account.user.email


class Tag(models.Model) :
    name = models.CharField(default="", max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="tags", null=True)
    
    
class Routine(models.Model) :
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="routines", null=True)
    week = models.IntegerField(default=0)
    start = models.TimeField(null=True)
    end = models.TimeField(null=True)

    def get_teacher_name(self) :
        return self.teacher.get_name
    
    def get_week_name(self) :
        week_list = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日"]
        return week_list[self.week]
    
        

class Schedule(models.Model) :
    routine = models.OneToOneField(Routine, on_delete=models.CASCADE, related_name="schedule", null=True)
    date = models.DateField(null=True)

    def get_teacher_name(self) :
        return self.routine.get_teacher_name
    

class Booking(models.Model) :
    student = models.OneToOneField(Account, on_delete=models.CASCADE, related_name="bookibg", null=True)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE, related_name="booking", null=True)

    def get_student_name(self) :
        return self.student.name

    def get_teacher_name(self) :
        return self.schedule.get_teacher_name
    
    def get_schedule_data(self) :
        return self.schedule.date