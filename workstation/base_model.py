from django.db import models


class Base(models.Model):
    criado = models.DateField(auto_now_add=True)
    editado = models.DateField(auto_now=True)

    class Meta:
        abstract = True
