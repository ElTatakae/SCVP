from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
#from .forms import registroAdministradorForm, ingresoAdminForm
#from django.views.decorators.csrf import csrf_protect
#from django.views.decorators.csrf import csrf_exempt


#@csrf_exempt
#@csrf_protect #Esto asegura que la validación del token CSRF se realice antes de procesar cualquier solicitud POST a esta vista.
def registro_de_usuario(request):
    template = loader.get_template('registro/registro_de_usuario.html')
    return HttpResponse(template.render())

def registro_de_administrador(request):
    template = loader.get_template('registro/registro_de_administrador.html')
    return HttpResponse(template.render())



def panel_administrador(request):
    template = loader.get_template('panel_administrador.html')
    return HttpResponse(template.render())



def modulo_administrador(request):
    template = loader.get_template('modulo_administrador.html')
    return HttpResponse(template.render())



def registro_de_empresa(request):
    template = loader.get_template('registro/registro_de_empresa.html')
    return HttpResponse(template.render())
