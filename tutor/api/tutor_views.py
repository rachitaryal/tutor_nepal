from tutor.models import Tutor
from tutor.paginations import TutorPagination
from tutor.serializers import TutorSerializer
from global_app.api.dfr_views import DRFListCreateView, DRFRetrieveUpdateDestroyView


class TutorBase:
    model = Tutor
    serializer_class = TutorSerializer
    pagination_class = TutorPagination



class TutorView(TutorBase, DRFListCreateView):
    pass


class TutorDetailView(TutorBase, DRFRetrieveUpdateDestroyView):
    pass
