from global_app.api.dfr_views import DRFListCreateView, DRFRetrieveUpdateDestroyView
from tutor.models import TutorCourseGrade
from tutor.paginations import TutorCourseGradePagination
from tutor.serializers import TutorCourseGradeSerializer


class TutorCourseGradeBase:
    model = TutorCourseGrade
    serializer_class = TutorCourseGradeSerializer
    pagination_class = TutorCourseGradePagination


class TutorCourseGradeView(TutorCourseGradeBase, DRFListCreateView):
    def get_queryset(self):
        """
        overridden function from drf_views.GlobalListAPIView to handle course_id and grade_id query
        """
        filter_kwargs = dict()
        course = self.request.query_params.get('course', None)
        grade = self.request.query_params.get('grade', None)
        if not course and grade:
            return self.model.objects.all()
        if course:
            filter_kwargs['course'] = course
        if grade:
            filter_kwargs['grade'] = grade
        try:
            return self.model.objects.filter(**filter_kwargs)
        except self.model.DoesNotExist:
            pass


class TutorCourseGradeDetailView(TutorCourseGradeBase, DRFRetrieveUpdateDestroyView):
    pass
