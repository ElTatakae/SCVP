from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def inicio_ingreso(request):
    template = loader.get_template('inicio_ingreso.html')
    return HttpResponse(template.render())


