from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ProdutosSerializer
from .models import Produtos


class ProdutosList(generics.ListCreateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    filter_backends = [DjangoFilterBackend, ]
    search_fields = [
        'nome',
    ]


class ProdutosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    filter_backends = [DjangoFilterBackend, ]
