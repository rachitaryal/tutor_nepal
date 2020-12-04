from course.models import CourseGrade
from course.serializers import CourseGradeSerializer
from global_app.api.dfr_views import DRFListCreateView, DRFRetrieveUpdateDestroyView


class CourseGradeBase:
    model = CourseGrade
    serializer_class = CourseGradeSerializer


class CourseGradeView(CourseGradeBase, DRFListCreateView):
    def get_queryset(self):
        """
        overridden function from drf_views.GlobalListAPIView to handle course_id query
        """
        filter_kwargs = dict()
        course = self.request.query_params.get('course', None)
        if not course:
            return self.model.objects.all()
        if course:
            filter_kwargs['course'] = course
        try:
            return self.model.objects.filter(**filter_kwargs)
        except self.model.DoesNotExist:
            pass


class CourseGradeDetailView(CourseGradeBase, DRFRetrieveUpdateDestroyView):
    pass
