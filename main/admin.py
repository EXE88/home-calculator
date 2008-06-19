from django.contrib import admin
from .models import ProjectInputs

@admin.register(ProjectInputs)
class ProjectInputsAdmin(admin.ModelAdmin):
    list_display = ('id','title','created')

