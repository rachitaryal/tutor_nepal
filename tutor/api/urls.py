from django.urls import path

from tutor.api import tutor_views, tutor_course_grade_views

urlpatterns = [
    # Tutor
    path('', tutor_views.TutorView.as_view(), name="tutor"),
    path('<int:pk>/', tutor_views.TutorDetailView.as_view(), name="tutor-detail"),

    # TutorCourseGrade
    path('tutor-course-grade/', tutor_course_grade_views.TutorCourseGradeView.as_view(), name="tutor-course-grade"),
    path('tutor-course-grade/<int:pk>/', tutor_course_grade_views.TutorCourseGradeDetailView.as_view(), name="tutor-course-grade-detail"),
]
