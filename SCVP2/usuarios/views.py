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

def base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

def modulo_lider(request):
    template = loader.get_template('modulo_lider.html')
    return HttpResponse(template.render())

def modulo_administrador(request):
    template = loader.get_template('modulo_administrador.html')
    return HttpResponse(template.render())

def modulo_operador(request):
    template = loader.get_template('modulo_operador.html')
    return HttpResponse(template.render())

def inicio(request):
    template = loader.get_template('landingpage.html')
    return HttpResponse(template.render())
