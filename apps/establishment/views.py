from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Establishment
from .serializers import EstablishmentSerializer

class EstablishmentViewSet(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    