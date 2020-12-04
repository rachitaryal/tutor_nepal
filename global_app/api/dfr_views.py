from rest_framework import generics
from rest_framework.response import Response
from rest_framework import authentication, permissions


class DRFBase:
    """ Provide the model, serializer_class, pagination_class & ---->lookup for more in ListCreateAPIView<----
        DRFBase class is made only to share common attribute and behavior among classes
    """
    model = None

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class DRFListCreateView(DRFBase, generics.ListCreateAPIView):
    """ you can use this view to create and list """
    pass


class DRFRetrieveUpdateDestroyView(DRFBase, generics.RetrieveUpdateDestroyAPIView):
    """ you can use this view to retrieve, update and destroy """
    pass


class DRFCreateView(DRFBase, generics.CreateAPIView):
    """you can use this view to create"""
    def get_serializer(self, *args, **kwargs):
        """
        Overriden from GenericAPIView / added the first line/ to make many = true
        """
        # kwargs['many'] = True
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class DRFListView(DRFBase, generics.ListAPIView):
    """ you can use this view to list"""
    pass


class DRFRetrieveView(DRFBase, generics.RetrieveAPIView):
    """ you can use this view to retrieve"""
    pass


class DRFDestroyView(DRFBase, generics.DestroyAPIView):
    """ you can use this view to destroy"""
    pass


class DRFUpdateView(DRFBase, generics.UpdateAPIView):
    """ you can use this view to update """
    pass
