from django.shortcuts import render
from django.utils import timezone
from .models import Student, Instructor, Lessons, Custodian
from django.utils import timezone
from .forms import StudentForm
from django.shortcuts import redirect

def dashboard(request):
    return render(request, 'index.html', {})

def students_list(request):
    list_students = Student.objects.filter(created__lte=timezone.now()).order_by("created")
    return render(request,'students_list.html', {'list_students':list_students})

def post_new(request):

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            #student = form.save(commit=False)
            #student.tc = request.tc
            #student.first_name = request.first_name
            #student.last_name = request.last_name
            #student.address = request.address
            #student.birthday = request.birthday
            #student.school = request.school
            #student.phone_no = request.phone_no
            #student.email = request.email
            #student.created = timezone.now()
            form.save()
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'student_edit.html', {'form': form})