from django.contrib import admin

from .models import Student, Instructor, Lessons, Custodian

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Lessons)
admin.site.register(Custodian)