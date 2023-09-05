from django.db import models
from locations.models import Location


class Connector(models.Model):
    """Charging connectors"""
    connector_type = models.CharField(max_length=100, help_text='Output connector name')

    def __str__(self) -> str:
        return f'{self.id} - {self.connector_type}'


class Station(models.Model):
    """Charging station (connected with Connector and Location)"""
    manufacturer = models.CharField(max_length=150, help_text='manufacturer name')
    available = models.BooleanField(default=True, help_text='True - yes, False - no')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False, related_name='stations')
    connectors = models.ManyToManyField(Connector, help_text='One station can have multiple connectors')

    def __str__(self) -> str:
        connectors_str = ', '.join([str(connector) for connector in self.connectors.all()])
        return f'{self.manufacturer}; Connectors: {connectors_str}'
