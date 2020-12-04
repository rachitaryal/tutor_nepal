from rest_framework import serializers

from course.models import Course, CourseGrade


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Course
        fields = '__all__'


class CourseGradeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = CourseGrade
        fields = ['id', 'course', 'grade', 'grade_name']
