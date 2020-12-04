from django.db import models


class Grade(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True, unique=True)
    description = models.TextField(default="Course...", null=True, blank=True)
    display_img = models.ImageField(null=True, blank=True)
    flag = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class CourseGrade(models.Model):
    course = models.ForeignKey(Course, models.CASCADE, related_name="course")
    grade = models.ForeignKey(Grade, models.CASCADE, related_name="grade")

    def __str__(self):
        return f"{self.course.name} - {self.grade.name}"

    @property
    def grade_name(self):
        return self.grade.name

    class Meta:
        unique_together = ('course', 'grade',)



