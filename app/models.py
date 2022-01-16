from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models.base import ModelState
from django.db.models.fields import AutoField, CharField
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = models.CharField(verbose_name='Adınız',max_length=30, blank=False)
    
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    is_student = models.BooleanField(default=True)
    is_custodian = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    tc = models.PositiveIntegerField(verbose_name='Öğrenci TC', validators=[MaxValueValidator(99999999999)])
    
    first_name = models.CharField(verbose_name='Öğrenci Adı',max_length=30, blank=False)
    last_name = models.CharField(verbose_name='Öğrenci Soyadı',max_length=20, blank=False)
    birthday = models.DateField(verbose_name='Öğrencinin Doğum Rarihi',max_length=8, blank=True) # sınırlamalar koy
    address = models.CharField(verbose_name='Öğrencinin Adresi',max_length=300, blank=True)
    email = models.EmailField(verbose_name='Öğrencinin e-Posta',blank=True) # null kullanmama gerek var mı ?
    school = models.CharField(verbose_name='Öğrencinin Okulu',max_length=30, blank=True)
    phone_no = models.PositiveIntegerField(verbose_name='Öğrencinin GSM',validators=[MaxValueValidator(9999999999)])
    created = models.DateTimeField(auto_now_add=True) 
    
    
    #Bağlantılar
    s_custodian = models.ManyToManyField('Custodian', verbose_name='Öğrencinin Velisi',max_length=30, blank=True)
    s_lessons = models.ManyToManyField('Lessons', verbose_name='Öğrencinin Dersleri',blank=True) 
    
    # yarışmalar, arkadaşlar, paylaşımlar, ödüller, rozetler

    

    def FindAge(self):
        age =datetime.date.today()-self.birthday
        full_age = int((age).days/365.25)
        return full_age

    FindAge.short_description = "Yaş"
        
        
    def full_name(self):
        #x=' '
        #name= self.first_name + x +self.last_name 
        #return name
        fullname = "%s %s" % (self.first_name, self.last_name)
        return fullname

    class Meta:
        verbose_name = 'Öğrenci'
        verbose_name_plural = 'Öğrenciler'
        ordering = ['first_name','last_name']
        
        
        


class Instructor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    is_student = models.BooleanField(default=False)
    is_custodian = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=True)

    tc = models.PositiveIntegerField(verbose_name='Eğitmen TC', validators=[MaxValueValidator(99999999999)])
    first_name = models.CharField(verbose_name='Eğitmen Adı',max_length=30,blank=False)
    last_name = models.CharField(verbose_name='Eğitmen Soyadı',max_length=20,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    #Bağlantılar
    i_lessons = models.ManyToManyField('Lessons',verbose_name='Eğitmenin Dersleri',blank=True) 
    
    i_students = models.ManyToManyField('Student', verbose_name='Eğitmenin Öğrencileri', blank=True)
    
    

    class Meta:
        verbose_name = 'Eğitmen'
        verbose_name_plural = 'Eğitmenler'
        ordering = ['first_name', 'last_name']

class Lessons(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    #Bağlantılar
    l_instructor_groups = models.ManyToManyField('Instructor',related_name="instructors",blank=True) 
    l_student = models.ManyToManyField('Student',verbose_name='Dersin Öğrencisi',blank=True)
    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Atölye'
        verbose_name_plural = 'Atölyeler'
        ordering = ['name']


class Custodian(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=1)
    is_student = models.BooleanField(default=False)
    is_custodian = models.BooleanField(default=True)
    is_instructor = models.BooleanField(default=False)

    tc = models.PositiveIntegerField(verbose_name='Veli tc',validators=[MaxValueValidator(99999999999)])
    first_name = models.CharField(verbose_name='Veli adı',max_length=30,blank=True)
    last_name = models.CharField(verbose_name='Veli soyadı',max_length=20,blank=True)
    
    #Bağlantılar
    c_students =  models.ManyToManyField('Student',verbose_name='Velinin Öğrencisi')
    

    def __str__(self):
        #x=' '
        #name= self.first_name + x +self.last_name 
        #return name 
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Veli'
        verbose_name_plural = 'Veliler'
        ordering = ['first_name', 'last_name']

        

        