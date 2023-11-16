from django.db import models
from entidade.models import Empresa

class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.DO_NOTHING)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome