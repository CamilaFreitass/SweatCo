from django.db import models

class Empresa(models.Model):
    nome_emp = models.CharField(max_length=50)
    email_adm = models.EmailField(unique=True)
    num_func = models.IntegerField()
    area_atua = models.CharField(max_length=50)
    senha = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_emp
