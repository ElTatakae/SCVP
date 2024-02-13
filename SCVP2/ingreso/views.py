from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def inicio_ingresoaa(request):
    template = loader.get_template('inicio_ingreso.html')
    return HttpResponse(template.render())

def ingreso_admin(reques):
    template = loader.get_template('ingreso_admin.html')
    return HttpResponse(template.render())

from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def ingreso(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Continuar con las redirecciones según el tipo de usuario
            if user.is_staff:
                return redirect('modulo_operador')
            elif user.is_superuser:
                return redirect('modulo_lider')
        else:
            # Autenticación fallida, mostrar un mensaje de error
            error_message = "Credenciales inválidas. Por favor, intenta de nuevo."
            return render(request, 'inicio_ingreso.html', {'error': error_message})
    return render(request, 'inicio_ingreso.html')




def modulo_operador(request):
    template = loader.get_template('modulo_operador.html')
    return HttpResponse(template.render())

def modulo_lider(request):
    template = loader.get_template('modulo_lider.html')
    return HttpResponse(template.render())