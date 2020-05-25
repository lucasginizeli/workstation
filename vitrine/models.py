from workstation.base_model import *


class Produtos(Base):
    nome = models.CharField(max_length=255, null=False, blank=False)
    info = models.TextField(max_length=None, null=False, blank=False)
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    imagem = models.ImageField(upload_to='uploads/')

    class Meta:
        db_table = 'produtos'
