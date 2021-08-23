from django.shortcuts import render
from .models import Student, Instructor, Lessons, Custodian

def dashboard(request):
    return render(request, 'index.html', {})
