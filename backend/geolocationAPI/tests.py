import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import responses

from .ipstack import API_ACCESS_KEY, URL
from .views import LocationInfo
from .ipstack import IpClient


class TestLocationInfo(APITestCase):
    def setUp(self):
        self.ip = "213.134.170.24"
        self.url = URL.format(ip=self.ip, api_access_key=API_ACCESS_KEY)
        self.mock_location = {
            "ip": self.ip,
            "type": "ipv4",
            "continent_code": "EU",
            "continent_name": "name",
            "country_code": "code",
            "country_name": "country",
            "region_code": "cd",
            "region_name": "region",
            "city": "city",
            "zip": "zip",
            "latitude": 1.0,
            "longitude": 1.0,
        }

    @responses.activate
    def test_should_return_mock_location_when_create_from_ipstack(self):
        responses.add(responses.GET, self.url, json=self.mock_location, status=200)

        response = self.client.post(
            reverse("locations-list"),
            json.dumps({"enter_ip": self.ip}),
            content_type="application/json",
        )

        self.assertEqual(response.data, self.mock_location)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @responses.activate
    def test_should_return_ip_exist_when_create_location(self):
        responses.add(responses.GET, self.url, json=self.mock_location, status=200)
        geolocation_1 = LocationInfo.objects.create(**self.mock_location)

        json_response = self.client.post(
            reverse("locations-list"),
            json.dumps({"enter_ip": self.ip}),
            content_type="application/json",
        )
        output = json_response.json()[0]

        self.assertEqual(output, "IP address already exists in DB")
        self.assertEqual(json_response.status_code, status.HTTP_400_BAD_REQUEST)

    @responses.activate
    def test_should_return_not_valid_ip_when_create_location(self):
        responses.add(responses.GET, self.url, json=self.mock_location, status=200)
        not_valid_ip = "123"

        json_response = self.client.post(
            reverse("locations-list"),
            json.dumps({"enter_ip": not_valid_ip}),
            content_type="application/json",
        )
        output = json_response.json().get("enter_ip")[0]

        self.assertEqual(output, "Enter a valid IPv4 or IPv6 address.")
        self.assertEqual(json_response.status_code, status.HTTP_400_BAD_REQUEST)

    @responses.activate
    def test_should_return_location_data_when_get_location_from_ipstack(self):
        responses.add(responses.GET, self.url, json=self.mock_location, status=200)

        location_data = IpClient.get_location_from_ipstack(ip=self.ip)

        self.assertEqual(location_data, self.mock_location)
