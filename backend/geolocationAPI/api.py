from rest_framework.routers import DefaultRouter
from .views import ViewSetIP, LocInfoViewSet


router = DefaultRouter()

router.register(r"locations", ViewSetIP, basename="locations")
router.register(r"loc", LocInfoViewSet, basename="locations")


location_urlpatterns = router.urls
