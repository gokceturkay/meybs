from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students_list.html', views.students_list, name='students_list'),
    path('student/edit', views.post_new, name='post_new'),
    path('student_panel.html', views.student_panel, name='student_panel'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/instructor/', instractors.TeacherSignUpView.as_view(), name='teacher_signup'),

]

































