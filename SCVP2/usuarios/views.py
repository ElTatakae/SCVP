from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt




def inicio_panel(request):
    template = loader.get_template('inicio_panel.html')
    return HttpResponse(template.render())


def inicio_de_sesion(request):
    template = loader.get_template('inicio_de_sesion.html')
    return HttpResponse(template.render())

def agregar_grupo(request):
    template = loader.get_template('agregar_grupo.html')
    return HttpResponse(template.render())

def base(request):
    template = loader.get_template('panel.html')
    return HttpResponse(template.render())

def panel_lideres(request):
    template = loader.get_template('panel_lideres.html')
    return HttpResponse(template.render())

def panel_operadores(request):
    template = loader.get_template('panel_operadores.html')
    return HttpResponse(template.render())