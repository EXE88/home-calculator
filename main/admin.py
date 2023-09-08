from django.contrib import admin
from .models import ProjectInputs
from django.contrib.auth.models import User

@admin.register(ProjectInputs)
class ProjectInputsAdmin(admin.ModelAdmin):
    list_display = ('id','title','created','user')
