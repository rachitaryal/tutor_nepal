from rest_framework import serializers

from tutor.models import Tutor, TutorCourseGrade


class TutorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Tutor
        fields = '__all__'


class TutorCourseGradeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = TutorCourseGrade
        fields = ['id', 'tutor', 'course', 'grade', 'tutor_name', 'tutor_info']
