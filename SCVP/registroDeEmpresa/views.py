from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.
def registroDeEmpresa(request):
    template = loader.get_template('registroDeEmpresa.html')
    return HttpResponse(template.render())

def registroNombreEmpresa(request):
    template = loader.get_template('registroNombreEmpresa.html')
    return HttpResponse(template.render())
def registroDatosEmpresa(request):
    template = loader.get_template('registroDatosEmpresa.html')
    return HttpResponse(template.render())