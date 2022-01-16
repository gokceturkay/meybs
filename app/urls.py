from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('hesap/', include('django.contrib.auth.urls')),
    path('kayit', views.login_view, name='login.html'),
    path('panel', views.panel, name='panel'),
    path('students_list', views.students_list, name='students_list'),
    path('student/edit', views.post_new, name='post_new'),
    path('student_panel', views.student_panel, name='student_panel'),
]































