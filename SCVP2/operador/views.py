from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def operador(request):
    context = {}
    return render(request, 'modulo_operador.html', context) #asegurarnos de que el contexto incluya el token CSRF con render


def estadisticos(request):
    template = loader.get_template('estadistico/estadisticos.html')
    return HttpResponse(template.render())

def crear_producto(request):
    template = loader.get_template('producto/crear_producto.html')
    return HttpResponse(template.render())

def panel_operador(request):
    context = {}
    return render(request, 'panel/panel_operador.html', context) #asegurarnos de que el contexto incluya el token CSRF con render

