from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader



# Create your views here.
def registroDeEmpresa(request):
    template = loader.get_template('registroDeEmpresa.html')
    return HttpResponse(template.render())

def registrarNombreEmpresa(request):
    template = loader.get_template('registrarNombreEmpresa.html')
    return HttpResponse(template.render())