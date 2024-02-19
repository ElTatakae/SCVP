from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def modulo_lider(request):
    context = {}
    return render(request, 'modulo_lider.html', context) #asegurarnos de que el contexto incluya el token CSRF con render

def crear_grupo(request):
    context = {}
    return render(request, 'crear_grupo.html', context) #asegurarnos de que el contexto incluya el token CSRF con render

def registro_de_lideres_y_operadores(request):
    context = {}
    return render(request, 'registro/registro_de_lideres_y_operadores.html', context) #asegurarnos de que el contexto incluya el token CSRF con render

def procesos(request):
    context = {}
    return render(request, 'procesos.html', context) #asegurarnos de que el contexto incluya el token CSRF con render
