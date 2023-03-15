from django.contrib import admin

# Register your models here.
from .models import *

class taskAdmin(admin.ModelAdmin):
    list_display=('id','title','taskContent','complete','dateOfCreated')
    list_filter=('dateOfCreated','title')
    search_fields=('title',)
    ordering=('dateOfCreated',)

admin.site.register(Task, taskAdmin)