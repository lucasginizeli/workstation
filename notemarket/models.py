from workstation.base_model import *


class Inventario(Base):
    descricao = models.CharField(max_length=255, null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'inventario'
