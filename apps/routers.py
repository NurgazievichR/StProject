from rest_framework import routers

from apps.establishment.views import EstablishmentViewSet
from apps.product.views import ProductViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('establishment', EstablishmentViewSet)

urlpatterns = router.urls