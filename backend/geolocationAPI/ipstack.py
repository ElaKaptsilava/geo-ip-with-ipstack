import requests

from typing import final

API_ACCESS_KEY = "2f1136f632bd172a75a0ef1a51040d93"
URL: final = "http://api.ipstack.com/{ip}?access_key={api_access_key}"


def get_location_from_ipstack(ip: str, key: str = API_ACCESS_KEY) -> dict:
    complete_url = URL.format(ip=ip, api_access_key=key)
    get_from_ip_stack = requests.get(complete_url).json()
    location_data = {
        "ip": get_from_ip_stack.get("ip"),
        "type": get_from_ip_stack.get("type"),
        "continent_code": get_from_ip_stack.get("continent_code"),
        "continent_name": get_from_ip_stack.get("continent_name"),
        "country_code": get_from_ip_stack.get("country_code"),
        "country_name": get_from_ip_stack.get("country_name"),
        "region_code": get_from_ip_stack.get("region_code"),
        "region_name": get_from_ip_stack.get("region_name"),
        "city": get_from_ip_stack.get("city"),
        "zip": get_from_ip_stack.get("zip"),
        "latitude": get_from_ip_stack.get("latitude"),
        "longitude": get_from_ip_stack.get("longitude"),
    }
    return location_data
