from django.contrib import admin
from .models import *

def register_admin(model):
    class ModelAdmin(admin.ModelAdmin):
        model = model

    return ModelAdmin

models = [Account, Tag, Teacher, Routine, Schedule, Booking]

for model in models:
    admin.site.register(model, register_admin(model))