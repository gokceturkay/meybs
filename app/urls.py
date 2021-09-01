from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students_list.html', views.students_list, name='students_list'),
]