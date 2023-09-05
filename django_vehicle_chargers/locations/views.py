# from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django.views import generic

from .models import Location


def index(request):
    return render(request, 'index.html')


def plug_share(request):
    return render(request, 'plug_share.html')


class LocationListView(generic.ListView):
    model = Location
    context_object_name = 'location_list'

    queryset = Location.objects.order_by("address")

    template_name = 'location/location_list.html'
