from django.contrib import admin

from .models import Connector, Station


class ConnectorAdmin(admin.ModelAdmin):
    pass


class StationAdmin(admin.ModelAdmin):
    filter_horizontal = ['connectors']


admin.site.register(Connector, ConnectorAdmin)
admin.site.register(Station, StationAdmin)
