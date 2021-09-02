from django import forms
from .models import Student
from django.forms import ModelForm



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("first_name" ,"last_name","birthday","address","school","phone_no","email")