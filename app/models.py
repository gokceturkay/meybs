from django.db import models
from django.db.models.base import ModelState
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
import datetime



class Student(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    birthday = models.DateField(max_length=8, blank=True) # sınırlamalar koy
    custodian = models.CharField(max_length=30, blank=False)
    tc = models.PositiveBigIntegerField(max_length=11, primary_key=True) 
    address = models.CharField(max_length=300,blank=True)
    email = models.EmailField(blank=True) # null kullanmama gerek var mı ?
    school = models.CharField(max_length=30,blank=True)
    phone_no = models.PositiveBigIntegerField(max_length=10)
    created = models.DateTimeField(auto_now_add=True) 
    # yarışmalar, arkadaşlar, paylaşımlar, ödüller, rozetler
    

    def FindAge(self):
        age =datetime.date.today()-self.birthday
        return int((age).days/365.25)
        
    def __str__(self):
        return self.first_name, self.last_name







class Instructor(models.Model):
    first_name = models.CharField(max_length=30,blank=False)
    last_name = models.CharField(max_length=20,blank=False)
    lessons = models.ForeignKey('Lessons', on_delete=models.CASCADE,blank=False) # foreginkey :,,,,(
    tc = models.PositiveBigIntegerField(max_length=11, primary_key=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    students = models.ForeignKey('Student', on_delete=models.CASCADE)
    # paylaşımlar, diğer bilgiler istenmemiş








class Lessons(models.Model):
    name = models.CharField(max_length=40)
    instructor = ForeignKey('Instructor', on_delete=models.CASCADE)
    student = ForeignKey('Student', on_delete=models.CASCADE)  


    def __str__(self):
        return self.name






class Custodian(models.Model):
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    tc = models.PositiveBigIntegerField(max_length=11, primary_key=True,blank=True)
    students =  ForeignKey('Student', on_delete=models.CASCADE)  

    def __str__(self):
         return self.first_name, self.last_name 









