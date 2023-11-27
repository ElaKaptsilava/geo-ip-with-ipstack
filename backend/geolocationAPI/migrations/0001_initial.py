# Generated by Django 3.2.23 on 2023-11-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="LocationInfo",
            fields=[
                ("ip", models.GenericIPAddressField(primary_key=True, serialize=False)),
                (
                    "type",
                    models.CharField(
                        choices=[("ipv4", "IPv4"), ("ipv6", "IPv6")], max_length=4
                    ),
                ),
                ("continent_code", models.CharField(max_length=2)),
                ("continent_name", models.CharField(max_length=20)),
                ("country_code", models.CharField(max_length=10)),
                ("country_name", models.CharField(max_length=50)),
                ("region_code", models.CharField(max_length=2)),
                ("region_name", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("zip", models.CharField(max_length=10)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
            options={
                "abstract": False,
            },
        ),
    ]