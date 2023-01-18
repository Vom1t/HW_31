import json


from django.db.models import Q
from django.http import JsonResponse, Http404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Ad
from ads.permissions import AdOwnerPermission
from ads.serializers import AdListSerializer, AdPostSerializer, AdPatchSerializer, AdDestroySerializer


def root(request):
    return JsonResponse({"status": "ok "})


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

    def get(self, request, *args, **kwargs):
        search_query = None

        params = {
            'cat': 'category__id__exact',
            'text': 'name__icontains',
            'location': 'author__location__name__icontains',
            'price_from': 'price__gte',
            'price_to': 'price__lte',
        }
        for param, value in dict(request.GET).items():
            data_filter = params.get(param, None)
            if data_filter:
                temp_dict = {data_filter: value[0]}
                if search_query is None:
                    search_query = Q(**temp_dict)
                else:
                    search_query |= Q(**temp_dict)
        if search_query:
            self.queryset = self.queryset.select_related('author').prefetch_related('category').filter(search_query).\
                order_by('-price')
        return super(AdListView, self).get(request, *args, **kwargs)


@method_decorator(csrf_exempt, name="dispatch")
@permission_classes((IsAuthenticated,))
class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdPostSerializer

    def create(self, request, *args, **kwargs):
        request.data['author'] = self.request.user.username
        return super().create(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer
    permission_classes = (IsAuthenticated, AdOwnerPermission)


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdPatchSerializer
    permission_classes = (IsAuthenticated, AdOwnerPermission)

@method_decorator(csrf_exempt, name="dispatch")
class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
    permission_classes = (IsAuthenticated, AdOwnerPermission)


@method_decorator(csrf_exempt, name="dispatch")
class AdImageView(UpdateView):
    model = Ad
    fields = ('name', 'image')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES['image']
        self.object.save()
        return JsonResponse(
            {
                'id': self.object.id,
                'name': self.object.name,
                'image': self.object.image.url
            }
        )
