from django import forms
from .models import Student



class StudentForm(forms.ModelForm):
    class Meta:
        Model = Student
        fields = ("firs_name" ,"last_name","birthday","address","school","phone_no","email")