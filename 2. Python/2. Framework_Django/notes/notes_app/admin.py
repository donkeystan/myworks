from django.contrib import admin

# Register your models here.
from .models import *

class NoteAdmin(admin.ModelAdmin):
    list_display=('id','Title','Content','Archived','DateOfCreate')
    list_filter=('DateOfCreate','Title')
    search_fields=('Title',)
    ordering=('DateOfCreate',)

admin.site.register(Note, NoteAdmin)