from django.contrib import admin
from .models import Note


# Register your models here.
class NodeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    
admin.site.register(Note, NodeAdmin)