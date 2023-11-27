import json

from django.urls import reverse
from rest_framework.test import APITestCase

import responses
from .ipstack import API_ACCESS_KEY, URL


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
    def test_create_from_ipstack(self, mock_location):
        responses.add(responses.GET, self.url, json=self.mock_location, status=200)

        request = self.client.post(
            reverse("locations-list"),
            json.dumps({"ip": self.ip}),
            content_type="application/json",
        )

        self.assertEqual(request.data, self.mock_location)
