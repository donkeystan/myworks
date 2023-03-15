from django import forms

class PostForm(forms.Form):
	title = forms.CharField(max_length=200, initial='')
	taskContent = forms.CharField(max_length=250, initial='')
	complete = forms.BooleanField()
	dateOfCreated = forms.DateTimeField()