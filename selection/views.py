from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from selection.models import Selection
from selection.permissions import SelectionOwnerPermission
from selection.serializers import SelectionSerializer, SelectionPostSerializer, SelectionDetailSerializer, \
    SelectionUpdateSerializer, SelectionDeleteSerializer


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionSerializer


@method_decorator(csrf_exempt, name="dispatch")
class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionPostSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request.data['owner'] = self.request.user.id
        return super().create(request, *args, **kwargs)


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


@method_decorator(csrf_exempt, name="dispatch")
class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionUpdateSerializer
    permission_classes = (IsAuthenticated, SelectionOwnerPermission)


@method_decorator(csrf_exempt, name="dispatch")
class SelectionDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDeleteSerializer
    permission_classes = (IsAuthenticated, SelectionOwnerPermission)
