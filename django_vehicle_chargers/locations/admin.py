from django.contrib.gis import admin as gis_admin

from .models import Location


@gis_admin.register(Location)
class LocationAdmin(gis_admin.GISModelAdmin):
    list_display = ("address", "location")

