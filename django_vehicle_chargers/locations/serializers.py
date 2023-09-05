from rest_framework_gis import serializers

from .models import Location


class LocationSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ("id", "address")
        geo_field = "location"
        model = Location
