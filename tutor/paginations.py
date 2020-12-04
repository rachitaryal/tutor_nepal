from rest_framework.pagination import PageNumberPagination


class TutorPagination(PageNumberPagination):
    page_size = 2

class TutorCourseGradePagination(PageNumberPagination):
    page_size = 1