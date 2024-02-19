from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from django.shortcuts import render

def ingreso_usuario(request):
    if request.method == 'POST':
        # Procesar los datos del formulario de inicio de sesión aquí
        # Verificar la autenticación del usuario, por ejemplo
        pass

    context = {}
    return render(request, 'ingreso_usuario.html', context)

def ingreso_administrador(request):
    if request.method == 'POST':
        # Procesar los datos del formulario de inicio de sesión para el administrador aquí
        # Verificar la autenticación del administrador, por ejemplo
        pass

    context = {}
    return render(request, 'ingreso_administrador.html', context)
