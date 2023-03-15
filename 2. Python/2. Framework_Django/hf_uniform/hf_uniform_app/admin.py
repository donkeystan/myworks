from django.contrib import admin

# Register your models here.
from .models import *

class UniformAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'CustName', 
                    'CustNo', 
                    'OrgnizationName', 
                    'Gender', 
                    'CustPhone', 
                    'CustEmail', 
                    'CustAddr', 
                    'DateOfCreated',
                   )
    list_filter = ('DateOfCreated','CustName',)
    search_fields = ('CustName',)
    ordering = ('-DateOfCreated',)

admin.site.register(Uniform, UniformAdmin)

'''
superuser:
name: admin
password: hofo1981

user:
name: danielliu
password: hofo1981

'''

'''

    CustName = models.CharField(max_length=20, null=False)
    CustNo = models.CharField(max_length=20, null=False)
    OrgnizationName = models.CharField(max_length=50, null=False)
    Gender = models.CharField(max_length=2, default='M', null=False)
    CustPhone = models.CharField(max_length=50, blank=True, default='')
    CustEmail = models.EmailField(max_length=100, blank=True, default='')
    CustAddr = models.CharField(max_length=255,blank=True, default='')
    DateOfCreated = models.DateField(auto_created=True)
    Hat = models.CharField(max_length=10, blank=True, default='')
    shoulder_width = models.CharField(max_length=10, blank=True, default='')
    sleeve_length = models.CharField(max_length=10, blank=True, default='')
    back_length = models.CharField(max_length=10, blank=True, default='')
    center_back = models.CharField(max_length=10, blank=True, default='')
    shirt_length = models.CharField(max_length=10, blank=True, default='')
    collar = models.CharField(max_length=10, blank=True, default='')
    chest = models.CharField(max_length=10, blank=True, default='')
    waist = models.CharField(max_length=10, blank=True, default='')
    seat = models.CharField(max_length=10, blank=True, default='')
    waist_belt = models.CharField(max_length=10, blank=True, default='')
    hip = models.CharField(max_length=10, blank=True, default='')
    crotch = models.CharField(max_length=10, blank=True, default='')
    front_crotch = models.CharField(max_length=10, blank=True, default='')
    thigh = models.CharField(max_length=10, blank=True, default='')
    pants_length = models.CharField(max_length=10, blank=True, default='')
    skirt_length = models.CharField(max_length=10, blank=True, default='')
    remark = models.CharField(max_length=30, blank=True, default='')

'Hat', 'shoulder_width', 'sleeve_length', 'back_length', 'center_back', 'shirt_length', 'collar', 'chest', 'waist', 'seat', 'waist_belt', 'hip', 'crotch', 'front_crotch', 'thigh', 'pants_length', 'skirt_length', 'remark')

'''