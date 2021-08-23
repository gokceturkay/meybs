from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.base import ModelState
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
import datetime

class Student(models.Model):
    first_name = models.CharField(verbose_name='Öğrenci Adı',max_length=30, blank=False)
    last_name = models.CharField(max_length=20, blank=False)
    birthday = models.DateField(max_length=8, blank=True) # sınırlamalar koy
    s_custodian = models.CharField(max_length=30, blank=False)
    tc = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    address = models.CharField(max_length=300, blank=True)
    email = models.EmailField(blank=True) # null kullanmama gerek var mı ?
    school = models.CharField(max_length=30, blank=True)
    phone_no = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    created = models.DateTimeField(auto_now_add=True) 
    # yarışmalar, arkadaşlar, paylaşımlar, ödüller, rozetler

    def FindAge(self):
        age =datetime.date.today()-self.birthday
        return int((age).days/365.25)
        
    def __str__(self):
        return self.first_name, self.last_name
    
    class Meta:
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'


class Instructor(models.Model):
    first_name = models.CharField(max_length=30,blank=False)
    last_name = models.CharField(max_length=20,blank=False)
    i_lessons = models.ForeignKey('Lessons', on_delete=models.CASCADE,blank=False) 
    tc = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    created = models.DateTimeField(auto_now_add=True)
    students = models.ForeignKey('Student', on_delete=models.CASCADE)
    # paylaşımlar, diğer bilgiler istenmemiş

    class Meta:
        verbose_name = 'Eğitmen'
        verbose_name_plural = 'Eğitmenler'

class Lessons(models.Model):
    name = models.CharField(max_length=40)
    l_instructor = ForeignKey('Instructor', on_delete=models.CASCADE)
    student = ForeignKey('Student', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Atölye'
        verbose_name_plural = 'Atölyeler'


class Custodian(models.Model):
    first_name = models.CharField(max_length=30,blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    tc = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(99999999999)])
    c_students =  ForeignKey('Student', on_delete=models.CASCADE)
    

    def __str__(self):
         return self.first_name, self.last_name 
    
    class Meta:
        verbose_name = 'Veli'
        verbose_name_plural = 'Veliler'