from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import InventarioSerializer
from .models import Inventario


class InventarioList(generics.ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    filter_backends = [DjangoFilterBackend, ]
    search_fields = [
        'descricao',
    ]


class InventarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
