from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def registro_de_empresa(request):
    template = loader.get_template('registro_de_empresa.html')
    return HttpResponse(template.render())


