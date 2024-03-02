from rest_framework import routers

from establishment.views import EstablishmentViewSet
from product.views import ProductViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('establishment', EstablishmentViewSet)

urlpatterns = router.urls