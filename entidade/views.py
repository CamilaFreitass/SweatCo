from django.shortcuts import render, redirect
from .models import Empresa
import json

def registro(request):
    return render(request, 'registro.html')

def valida_registro(request):
    data = json.loads(request.body)
    nome_emp = data.get('nome_emp')
    email_adm = data.get('email_adm')
    num_func = data.get('num_func')
    area_atua = data.get('area_atua')
    senha = data.get('senha')

    empresa = Empresa(nome_emp=nome_emp,
                      email_adm=email_adm,
                      num_func=num_func,
                      area_atua=area_atua,
                      senha=senha)
    empresa.save()
    return redirect('/entidade/registro/')
