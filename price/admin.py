from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    search_fields = ('name','group','brand',)
    list_display = ('id','name','group','brand',)
