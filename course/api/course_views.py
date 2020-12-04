from course.models import Course
from course.serializers import CourseSerializer
from global_app.api.dfr_views import DRFListCreateView, DRFRetrieveUpdateDestroyView


class CourseBase:
    model = Course
    serializer_class = CourseSerializer


class CourseView(CourseBase, DRFListCreateView):
    def get_queryset(self):
        """
        overridden function from drf_views.GlobalListAPIView to handle flagged_courses query
        check the query param for flag=True/False and return accordingly
        """
        filter_kwargs = dict()
        flag = self.request.query_params.get('flag', None)
        if not flag:
            return self.model.objects.all()
        if flag:
            filter_kwargs['flag'] = flag
        try:
            return self.model.objects.filter(**filter_kwargs)
        except self.model.DoesNotExist:
            pass


class CourseDetailView(CourseBase, DRFRetrieveUpdateDestroyView):
    pass
