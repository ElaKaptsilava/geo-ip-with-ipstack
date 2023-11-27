from rest_framework.routers import DefaultRouter
from .views import LocationInfoViewSet


router = DefaultRouter()

router.register(r"locations", LocationInfoViewSet, basename="locations")


location_urlpatterns = router.urls
