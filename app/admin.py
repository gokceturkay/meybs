from django.contrib import admin

from .models import Student, Instructor, Lessons, Custodian

import datetime






class  DetailsStudent(admin.ModelAdmin):

    list_display = (('first_name','last_name','get_custodian','get_lessons','FindAge'))

    def get_custodian(self, obj):
        return "\n".join([str(p)for p in obj.s_custodian.all()])
        
    
    def get_lessons(self, obj):
        return "\n".join([str(p)for p in obj.s_lessons.all()])
        

    Student.FindAge
    




class  DetailsInstructor(admin.ModelAdmin):
    list_display = (('first_name','last_name','get_lessons'))

    def get_lessons(self, obj):
        return "\n".join([str(p)for p in obj.i_lessons.all()])






class  DetailsLessons(admin.ModelAdmin):
    list_display = (('name','get_instructor','getStudents'))


    def get_instructor(self, obj):
        return "\n".join([str(p)for p in obj.l_instructor])
       #return Lessons.l_instructor (işe yaramıyor)

    def getStudents(self, obj):
        return "\n".join([str(p)for p in obj.l_student.all()])

    get_instructor.short_description = "Eğitmenler"
    getStudents.short_description = "Öğrenciler"


    






class DetailsCostodian(admin.ModelAdmin):
    list_display = (('first_name','last_name','get_students'))

    def get_students(self, obj):
        return "\n".join([str(p)for p in obj.c_students.all()])


admin.site.register(Student, DetailsStudent)
admin.site.register(Instructor, DetailsInstructor)
admin.site.register(Lessons, DetailsLessons)
admin.site.register(Custodian, DetailsCostodian)




