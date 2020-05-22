from rest_framework import generics

from .serializers import ProdutosSerializer
from .models import Produtos


class ProdutosList(generics.ListCreateAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer


class ProdutosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
