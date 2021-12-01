from django import forms
from .models import Student
from django.forms import ModelForm



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("tc","first_name" ,"last_name","birthday","address","school","phone_no","email")
        
class InfoForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    #lesson = 
    message = forms.CharField(widget=forms.Textarea)
    
    