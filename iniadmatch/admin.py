from django.contrib import admin
from .models import Account, Tag, Teacher, Schedule, Booking


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_gmail')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'get_gmail', 'tag')

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('get_teacher_name', 'get_week_name', 'start', 'end')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('get_student_name', 'get_teacher_name', 'get_schedule_data', 'get_teacher_tags')
