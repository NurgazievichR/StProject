from rest_framework import routers

from .views import EstablishmentViewSet

router = routers.DefaultRouter()
router.register('establishment', EstablishmentViewSet)
urlpatterns = router.urls