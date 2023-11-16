from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name="registro"),
    path('valida_registro/', views.valida_registro, name="valida_registro"),
]