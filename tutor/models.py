from django.db import models

from course.models import Course, Grade


class Tutor(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True)
    info = models.TextField(default="Teacher at Tutor Nepal")
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name


class TutorCourseGrade(models.Model):
    tutor = models.ForeignKey(Tutor, models.CASCADE, related_name="tutor")
    course = models.ForeignKey(Course, models.CASCADE)
    grade = models.ForeignKey(Grade, models.CASCADE)

    def __str__(self):
        return f"{self.tutor.name} - {self.course.name} - {self.grade.name}"

    @property
    def tutor_name(self):
        return self.tutor.name

    @property
    def tutor_info(self):
        return self.tutor.info

    class Meta:
        unique_together = ('tutor', 'course', 'grade',)