from django.contrib import admin
from .models import Material

class MaterialAdmin(admin.ModelAdmin):
    search_fields = ('name','group','brand',)
