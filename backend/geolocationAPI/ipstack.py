import requests
from .constants import URL, API_ACCESS_KEY


class IpClient:
    @staticmethod
    def get_location_from_ipstack(ip: str, key: str = API_ACCESS_KEY) -> dict:
        complete_url = URL.format(ip=ip, api_access_key=key)
        get_from_ip_stack = requests.get(complete_url)
        get_from_ip_stack.raise_for_status()
        json_data = get_from_ip_stack.json()

        location_data = {
            "ip": json_data.get("ip"),
            "type": json_data.get("type"),
            "continent_code": json_data.get("continent_code", ""),
            "continent_name": json_data.get("continent_name"),
            "country_code": json_data.get("country_code"),
            "country_name": json_data.get("country_name"),
            "region_code": json_data.get("region_code", ""),
            "region_name": json_data.get("region_name"),
            "city": json_data.get("city"),
            "zip": json_data.get("zip"),
            "latitude": json_data.get("latitude"),
            "longitude": json_data.get("longitude"),
        }

        return location_data
