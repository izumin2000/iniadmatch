from django.db import models
from social_django.models import UserSocialAuth



class Account(models.Model):
    name = models.CharField(max_length=255)
    usersocialauth = models.OneToOneField(UserSocialAuth, on_delete=models.CASCADE)

    def get_gmail(self):
        return self.usersocialauth.uid


class Student(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def get_name(self):
        return self.account.name
    
    def get_gmail(self):
        return self.account.usersocialauth.uid


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Teacher(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def get_name(self):
        return self.account.name
    
    def get_gmail(self):
        return self.account.usersocialauth.uid
        

class Schedule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()

    def get_teacher_name(self):
        return self.teacher.account.name
    

class Booking(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    date = models.DateField()
    comment = models.TextField()

    def get_student_name(self):
        return self.student.account.name

    def get_teacher_name(self):
        return self.schedule.teacher.account.name
    
    def get_schedule_data(self):
        return self.schedule.date
    
    def get_teacher_tags(self):
        return self.schedule.teacher.tag