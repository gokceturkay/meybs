from django.shortcuts import render
from django.utils import timezone
from .models import Student, Instructor, Lessons, Custodian
from django.utils import timezone

def dashboard(request):
    return render(request, 'index.html', {})

def students_list(request):
    list_students = Student.objects.filter(created__lte=timezone.now()).order_by("created")
    return render(request,'students_list.html', {'list_students':list_students})





