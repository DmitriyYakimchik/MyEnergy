from django.contrib.gis.db import models as gis_models
from django.urls import reverse


class Location(gis_models.Model):
    """Where the charging stations are located"""
    address = gis_models.CharField(max_length=255, help_text='Full address (street, city, international code)')
    location = gis_models.PointField()

    # latitude = house.location.coords[1]
    # longitude = house.location.coords[0]

    def __str__(self):
        return self.address

    def get_absolute_url(self, *args):
        """Returns the url to access a particular instance of the model."""
        return reverse('locations', args=args)
