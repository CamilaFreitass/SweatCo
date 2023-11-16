from django.shortcuts import render
from .models import Atividade
import json
from datetime import datetime
from perfil.models import Usuario
from django.http import JsonResponse

def registro(request):

    if request.method == "GET":
        return Atividade.objects.all()

    data = json.loads(request.body)
    tempo_atividade = data.get('tempo_atividade')
    usuario_instance = Usuario.objects.get(pk=data.get('usuario_id'))  # Fetching the Usuario instance with ID 1
    usuario_id = usuario_instance
    atividade_id = data.get('atividade_id')
    created_at = data.get('created_at')
    created_at = datetime.fromisoformat(data.get('created_at'))

    atividade = Atividade(
    tempo_atividade=tempo_atividade,
    usuario_id=usuario_id,
    atividade_id=atividade_id,
    created_at=created_at,
    )

    atividade.save()
    return JsonResponse({'message': 'Requisição processada com sucesso!'})
