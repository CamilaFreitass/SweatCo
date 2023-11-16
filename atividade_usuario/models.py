from django.db import models
from perfil.models import Usuario

class Atividade(models.Model):
    tempo_atividade = models.IntegerField()
    usuario_id = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    atividade_id = models.IntegerField()
    created_at = models.DateTimeField(max_length=50)
