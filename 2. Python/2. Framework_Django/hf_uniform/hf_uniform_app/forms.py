from django import forms
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

class PostForm(forms.Form):
    cust_name = forms.CharField(max_length=20,initial='')
    cust_no= forms.CharField(max_length=20,initial='',required=False)
    orgnization_name = forms.CharField(max_length=50,initial='',required=False)
    gender = forms.CharField(max_length=2,initial='M')
    cust_phone = forms.CharField(max_length=50,initial='',required=False)
    cust_email = forms.EmailField(max_length=100,initial='',required=False)
    cust_addr = forms.CharField(max_length=255,initial='',required=False)
    date_of_created = forms.DateField(widget=DatePickerInput)
    hat = forms.CharField(max_length=10,initial='',required=False)
    shoulder_width = forms.CharField(max_length=10,initial='',required=False)
    sleeve_length = forms.CharField(max_length=10,initial='',required=False)
    back_length = forms.CharField(max_length=10,initial='',required=False)
    center_back = forms.CharField(max_length=10,initial='',required=False)
    shirt_length = forms.CharField(max_length=10,initial='',required=False)
    collar = forms.CharField(max_length=10,initial='',required=False)
    chest = forms.CharField(max_length=10,initial='',required=False)
    waist = forms.CharField(max_length=10,initial='',required=False)
    seat = forms.CharField(max_length=10,initial='',required=False)
    waist_belt = forms.CharField(max_length=10,initial='',required=False)
    hip = forms.CharField(max_length=10,initial='',required=False)
    crotch = forms.CharField(max_length=10,initial='',required=False)
    front_crotch = forms.CharField(max_length=10,initial='',required=False)
    thigh = forms.CharField(max_length=10,initial='',required=False)
    pants_length = forms.CharField(max_length=10,initial='',required=False)
    skirt_length = forms.CharField(max_length=10,initial='',required=False)
    remark = forms.CharField(max_length=30,initial='',required=False)