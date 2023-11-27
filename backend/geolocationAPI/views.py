from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets, status

from .serializers import (
    LocationInfoSerializers,
    IPSerializers,
    MyTokenObtainPairSerializer,
    LocInfoSerializers,
)
from .ipstack import get_location_from_ipstack
from .models import LocationInfo

from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ViewSetIP(viewsets.ModelViewSet):
    serializer_class = IPSerializers
    queryset = LocationInfo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["ip"]

    def create(self, request, *args, **kwargs):
        ip_serializer = self.serializer_class(data=request.data)
        ip_serializer.is_valid(raise_exception=True)
        ip_param = ip_serializer.validated_data.get("ip", None)
        location_data = get_location_from_ipstack(ip=ip_param)
        location_with_api = LocationInfoSerializers(data=location_data)
        location_with_api.is_valid(raise_exception=True)
        location_with_api.save()
        return Response(location_with_api.data, status=status.HTTP_201_CREATED)


class LocInfoViewSet(viewsets.ModelViewSet):
    serializer_class = LocInfoSerializers
    queryset = LocationInfo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["ip"]
