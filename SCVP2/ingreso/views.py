from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def inicio_ingreso(request):
    template = loader.get_template('inicio_ingreso.html')
    return HttpResponse(template.render())

def ingreso_admin(reques):
    template = loader.get_template('ingreso_admin.html')
    return HttpResponse(template.render())


