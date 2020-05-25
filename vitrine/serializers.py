from rest_framework import serializers
from .models import Produtos


class ProdutosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produtos
        db_name = 'produtos'
        # fields = '__all__'
        fields = [
            'id',
            'nome',
            'info',
            'valor',
            'imagem'
        ]
