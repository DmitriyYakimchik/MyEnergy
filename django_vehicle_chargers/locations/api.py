from rest_framework import routers

from .viewsets import LocationViewSet

router = routers.DefaultRouter()
router.register(r"locations", LocationViewSet)

urlpatterns = router.urls
