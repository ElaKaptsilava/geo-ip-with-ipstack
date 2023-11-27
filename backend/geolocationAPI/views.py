from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .serializers import MyTokenObtainPairSerializer, LocationInfoSerializers
from .models import LocationInfo

from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class LocationInfoViewSet(viewsets.ModelViewSet):
    serializer_class = LocationInfoSerializers
    queryset = LocationInfo.objects.all()
    filter_backends = [DjangoFilterBackend]
