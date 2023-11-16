from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario
from entidade.models import Empresa

def cadastro(request):
    if request.method == "GET":
        empresas = Empresa.objects.all()

        return render(request, 'cadastro.html', {'empresas': empresas})
    else:
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        empresa = request.POST.get('empresa')
        senha = request.POST.get('senha')

        usuario = Usuario(nome=nome,
                      email=email,
                      empresa_id=empresa,
                      senha=senha)
        usuario.save()
        return redirect('/perfil/cadastro/')


 