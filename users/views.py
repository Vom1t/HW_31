
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet


from users.models import User, Locations
from users.serializers import LocationSerializer, UserSerializer, UserPostSerializer, UserUpdateSerializer, \
    UserDestroySerializer


class LocationViewSet(ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(csrf_exempt, name="dispatch")
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserPostSerializer


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer


@method_decorator(csrf_exempt, name="dispatch")
class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer

