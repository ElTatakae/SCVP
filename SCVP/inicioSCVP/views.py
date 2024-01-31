from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.
def inicioSCVP(request):
    template = loader.get_template('inicio.html')
    return HttpResponse(template.render())
def inicioAdministrador(request):
    template = loader.get_template('inicioAdministrador.html')
    return HttpResponse(template.render())

def creacionDeGrupo(request):
    template = loader.get_template('creacionDeGrupo.html')
    return HttpResponse(template.render())

def registroUsuario(request):
    template = loader.get_template('registroUsuario.html')
    return HttpResponse(template.render())

def agregarGrupo(request):
    template = loader.get_template('agregarGrupo.html')
    return HttpResponse(template.render())
