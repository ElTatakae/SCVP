from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def modulo_lider(request):
    context = {}
    return render(request, 'modulo_lider.html', context) #asegurarnos de que el contexto incluya el token CSRF con render

def crear_grupo(request):
    context = {}
    return render(request, 'grupo/crear_grupo.html', context) #asegurarnos de que el contexto incluya el token CSRF con render

def registro_de_lideres_y_operadores(request):
    context = {}
    return render(request, 'registro/registro_de_lideres_y_operadores.html', context) #asegurarnos de que el contexto incluya el token CSRF con render

def procesos(request):
    context = {}
    return render(request, 'proceso/procesos.html', context) #asegurarnos de que el contexto incluya el token CSRF con render

def producto(request):
    context = {}
    return render(request, 'producto/producto.html', context) #asegurarnos de que el contexto incluya el token CSRF con render

def monitoreo(request):
    context = {}
    return render(request, 'monitoreo.html', context) #asegurarnos de que el contexto incluya el token CSRF con render
