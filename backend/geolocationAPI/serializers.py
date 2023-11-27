from django.db import transaction
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


class LocationInfoSerializers(serializers.ModelSerializer):
    enter_ip = serializers.IPAddressField(write_only=True)

    class Meta:
        model = LocationInfo
        fields = "__all__"
        write_only_fields = ["enter_ip"]
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

    @transaction.atomic
    def create(self, validated_data):
        enter_ip = validated_data.get("enter_ip")
        if LocationInfo.objects.filter(ip=enter_ip):
            raise serializers.ValidationError("IP address already exists in DB")
        location_data = get_location_from_ipstack(ip=enter_ip)
        return LocationInfo.objects.create(**location_data)
