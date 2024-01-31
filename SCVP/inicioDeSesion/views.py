from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader




# Create your views here.
def inicioDeSesion(request):
    template = loader.get_template('logueo.html')
    return HttpResponse(template.render())

def registro(request):
    template = loader.get_template('registro.html')
    return HttpResponse(template.render())