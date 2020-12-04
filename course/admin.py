from django.contrib import admin
from course.models import Course, Grade,  CourseGrade

admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(CourseGrade)
