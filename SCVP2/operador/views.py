from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def estadisticos(request):
    template = loader.get_template('estadisticos.html')
    return HttpResponse(template.render())

def crear_producto(request):
    template = loader.get_template('crear_producto.html')
    return HttpResponse(template.render())
