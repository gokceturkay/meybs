from django.contrib import admin

from .models import Student, Instructor, Lessons, Custodian

import datetime




class  DetailsStudent(admin.ModelAdmin):
    list_display = (('first_name','last_name','get_custodian','get_lessons'))

    def get_custodian(self, obj):
        return "\n".join([str(p)for p in obj.s_custodian.all()])
        
    
    def get_lessons(self, obj):
        return "\n".join([str(p)for p in obj.s_lessons.all()])

    #def FindAge(self):
    #    age =datetime.date.today()-self.birthday
    #    return int((age).days/365.25)
    




class  DetailsInstructor(admin.ModelAdmin):
    list_display = (('first_name','last_name','get_lessons'))

    def get_lessons(self, obj):
        return "\n".join([str(p)for p in obj.i_lessons.all()])






#class  DetailsLessons(admin.ModelAdmin):
#   list_display = (('id','name','get_instructor','get_student'))


    #def get_instructor(self, obj):
        #return "\n".join([str(p)for p in obj.l_instructor.all()])


    #def get_student(self, obj):
        #return "\n".join([str(p)for p in obj.l_student.all()])






class DetailsCostodian(admin.ModelAdmin):
    list_display = (('first_name','last_name','get_students'))

    def get_students(self, obj):
        return "\n".join([str(p)for p in obj.c_students.all()])


admin.site.register(Student, DetailsStudent)
admin.site.register(Instructor, DetailsInstructor)
admin.site.register(Lessons)
admin.site.register(Custodian, DetailsCostodian)




