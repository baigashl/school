from django.contrib import admin
from .models import School, Teacher, Grade, Student

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Grade)
admin.site.register(Student)

