from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='location_page'),
    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('plug_share/', views.plug_share, name='plug_share'),
]
