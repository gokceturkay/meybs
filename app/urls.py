from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('stuents_list.html', views.students_list, name='students_list'),
]


