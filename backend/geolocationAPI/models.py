from django.db import models


class ModelsManager(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class LocationInfo(ModelsManager):
    ip = models.GenericIPAddressField(primary_key=True)
    type = models.CharField(max_length=4, choices=[("ipv4", "IPv4"), ("ipv6", "IPv6")])
    continent_code = models.CharField(max_length=2)
    continent_name = models.CharField(max_length=20)
    country_code = models.CharField(max_length=10)
    country_name = models.CharField(max_length=50)
    region_code = models.CharField(max_length=2)
    region_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    latitude = models.FloatField()
    longitude = models.FloatField()
