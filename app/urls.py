from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students_list.html', views.students_list, name='students_list'),
    path('student/edit', views.post_new, name='post_new'),
    path('student_panel.html', views.student_panel, name='student_panel'),
]































