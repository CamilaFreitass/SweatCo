from django.shortcuts import render, redirect
from .models import Empresa

def registro(request):
    return render(request, 'registro.html')

def valida_registro(request):
    nome_emp = request.POST.get('nome_emp')
    email_adm = request.POST.get('email_adm')
    num_func = request.POST.get('num_func')
    area_atua = request.POST.get('area_atua')
    senha = request.POST.get('senha')

    empresa = Empresa(nome_emp=nome_emp,
                      email_adm=email_adm,
                      num_func=num_func,
                      area_atua=area_atua,
                      senha=senha)
    empresa.save()
    return redirect('/entidade/registro/')