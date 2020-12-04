from django.urls import path

from course.api import course_views, course_grade_views

urlpatterns = [
    # Course
    path('', course_views.CourseView.as_view(), name="course"),
    path('<int:pk>/', course_views.CourseDetailView.as_view(), name="course-detail"),

    # CourseGrade
    path('course-grade/', course_grade_views.CourseGradeView.as_view(), name="course-grade"),
    path('course-grade/<int:pk>/', course_grade_views.CourseGradeDetailView.as_view(), name="course-grade-detail"),
]
