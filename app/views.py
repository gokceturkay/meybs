from django.shortcuts import render
from django.utils import timezone
from .models import Student, Instructor, Lessons, Custodian
from django.utils import timezone
from .forms import StudentForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth import get_user_model


def dashboard(request):
    return render(request, 'index.html', {})

def students_list(request):
    list_students = Student.objects.filter(created__lte=timezone.now()).order_by("created")
    return render(request,'students_list.html', {'list_students':list_students})

#### Burada uğraşıyoruz. Giriş yapanın adını çekmek istiyoruz

def student_panel(request):
    if request.user.is_authenticated:
        students_name = request.user.get_full_name()
        return render(request, 'spanel.html', {"students_name":students_name})
    else:
        return render(request, 'index.html', {})
def post_new(request):

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
           # student = form.save(commit=False)
           # student.first_name = request.first_name
           # student.last_name = request.last_name
           # student.address = request.address
           # student.birthday = request.birthday
           # student.school = request.school
           # student.phone_no = request.phone_no
           # student.email = request.email
           # student.created = timezone.now()
            form.save()
            messages.success(request,"öğrenci kaydedildi")
            return redirect('/')
    else:
        form = StudentForm()
    return render(request, 'student_edit.html', {'form': form})

#def login_view(request):
#    if request.method == 'POST':
#       username = request.POST.get('username')
#        password = request.POST.get('password')
#        user = authenticate(username=username, password=password)
#        if user:
#            if user.is_active:
#                login(request, user)
#                return HttpResponseRedirect('/panel/')
#            else:
#                return HttpResponse("Hesabını actif değil")
#        else:
#            print("Hatalı giriş bilgileri: {0}, {1}").format(username, password)
#            return HttpResponse("Hatalı giriş bilgileri alındı.")
#    else:
#        return render(request, 'registration/login.html', {}) 


#çalışılıyor
def panel(request):
    
    if Student.is_student:
        return HttpResponse("Öğrenci")
    else:
        return HttpResponse("Başka")
