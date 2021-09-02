from django.shortcuts import render
from django.utils import timezone
from .models import Student, Instructor, Lessons, Custodian
from django.utils import timezone
from .forms import StudentForm

def dashboard(request):
    return render(request, 'index.html', {})

def students_list(request):
    list_students = Student.objects.filter(created__lte=timezone.now()).order_by("created")
    return render(request,'students_list.html', {'list_students':list_students})

def post_new(request):
    form = StudentForm()
    return render(request, 'student_edit.html', {'form': form})





