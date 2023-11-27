from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import LocationInfo
from .ipstack import get_location_from_ipstack


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["username"] = user.username

        return token


class IPSerializers(serializers.ModelSerializer):
    class Meta:
        model = LocationInfo
        fields = ["ip"]


class LocationInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = LocationInfo
        fields = "__all__"


class LocInfoSerializers(serializers.ModelSerializer):
    ip_input = serializers.IPAddressField(write_only=True)

    class Meta:
        model = LocationInfo
        fields = "__all__"
        write_only_fields = ["ip_input"]
        read_only_fields = [
            "ip",
            "type",
            "continent_code",
            "continent_name",
            "country_code",
            "country_name",
            "region_code",
            "region_name",
            "city",
            "zip",
            "latitude",
            "longitude",
        ]

    def create(self, validated_data):
        ip_input = validated_data.get("ip_input")
        location_data = get_location_from_ipstack(ip=ip_input)
        return LocationInfo.objects.create(**location_data)
