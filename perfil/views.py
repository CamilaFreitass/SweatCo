from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from entidade.models import Empresa
import json

def cadastro(request):
    if request.method == "GET":
        empresas = Empresa.objects.all()

        return render(request, 'cadastro.html', {'empresas': empresas})
    else:
        data = json.loads(request.body)
        nome = data.get('nome')
        email = data.get('email')
        empresa = data.get('empresa')
        senha = data.get('senha')

        usuario = Usuario(nome=nome,
                      email=email,
                      empresa_id=empresa,
                      senha=senha)
        usuario.save()
        return redirect('/perfil/cadastro/')
