from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def ingreso_administrador(request):
    template = loader.get_template('ingreso_administrador.html')
    return HttpResponse(template.render())


