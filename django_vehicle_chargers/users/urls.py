from django.urls import path
from . import views

urlpatterns = [
    path("registration", views.register_request, name="register_request"),
    path('profile/', views.profile, name='profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile')
]
