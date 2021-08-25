from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.base import ModelState
from django.db.models.fields import AutoField, CharField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
import datetime

class Student(models.Model):
    first_name = models.CharField(verbose_name='Öğrenci Adı',max_length=30, blank=False)
    last_name = models.CharField(verbose_name='Öğrenci soyadı',max_length=20, blank=False)
    birthday = models.DateField(verbose_name='Öğrencinin doğum tarihi',max_length=8, blank=True) # sınırlamalar koy
    s_custodian = models.CharField(verbose_name='Öğrencinin velisi',max_length=30, blank=False)
    tc = models.PositiveIntegerField(verbose_name='Öğrenci tc',primary_key=True, validators=[MaxValueValidator(99999999999)])
    address = models.CharField(verbose_name='Öğrencinin adresi',max_length=300, blank=True)
    email = models.EmailField(verbose_name='Öğrencinin e-posta',blank=True) # null kullanmama gerek var mı ?
    school = models.CharField(verbose_name='Öğrencinin okulu',max_length=30, blank=True)
    phone_no = models.PositiveIntegerField(verbose_name='Öğrencinin numarası',validators=[MaxValueValidator(9999999999)])
    #s_lessons = models.ForeignKey('Lessons', verbose_name='Öğrencinin dersleri',on_delete=models.CASCADE) #beğenmedi :(
    created = models.DateTimeField(auto_now_add=True) 
    # yarışmalar, arkadaşlar, paylaşımlar, ödüller, rozetler

    def FindAge(self):
        age =datetime.date.today()-self.birthday
        return int((age).days/365.25)
        
    def __str__(self):
        x=' '
        name= self.first_name + x +self.last_name 
        return name
    
    class Meta:
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'


class Instructor(models.Model):
    first_name = models.CharField(verbose_name='Eğitmen adı',max_length=30,blank=False)
    last_name = models.CharField(verbose_name='Eğitmen soyadı',max_length=20,blank=False)
    #i_lessons = models.ForeignKey('Lessons',verbose_name='Eğitmenin dersleri', on_delete=models.CASCADE,blank=True,null=True) 
    tc = models.PositiveIntegerField(verbose_name='Eğitmen tc',primary_key=True, validators=[MaxValueValidator(99999999999)])
    created = models.DateTimeField(auto_now_add=True)
    #i_students = models.ForeignKey('Student', verbose_name='Eğitmenin öğrencileri',on_delete=models.CASCADE)
    # paylaşımlar, diğer bilgiler istenmemiş

    class Meta:
        verbose_name = 'Eğitmen'
        verbose_name_plural = 'Eğitmenler'

class Lessons(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    # l_instructor = ForeignKey('Instructor',verbose_name='Dersin eğitmeni', on_delete=models.CASCADE,)
    #l_student = ForeignKey('Student',verbose_name='Dersin öğrencisi', on_delete=models.CASCADE,null=False)


    def __str__(self):
        x=' '
        name= self.first_name + x +self.last_name 
        return name
    
    class Meta:
        verbose_name = 'Atölye'
        verbose_name_plural = 'Atölyeler'


class Custodian(models.Model):
    first_name = models.CharField(verbose_name='Veli adı',max_length=30,blank=True)
    last_name = models.CharField(verbose_name='Veli soyadı',max_length=20,blank=True)
    tc = models.PositiveIntegerField(verbose_name='Veli tc',primary_key=True, validators=[MaxValueValidator(99999999999)])
    #c_students =  ForeignKey('Student',verbose_name='Velinin öğrencisi', on_delete=models.CASCADE)
    

    def __str__(self):
        x=' '
        name= self.first_name + x +self.last_name 
        return name 
    
    class Meta:
        verbose_name = 'Veli'
        verbose_name_plural = 'Veliler'