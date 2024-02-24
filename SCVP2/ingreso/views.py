from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm



def ingresoaa(request):
    print (request.POST)
    print (request.POST.get('username'))
    print (request.POST.get('password'))
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

def ingreso_usuario(request):
    print(request.POST)
    if request.method == 'GET':
        return render(request, 'inicio_ingreso.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'inicio_ingreso.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña son incorrectos'
            })  
        else:
            login(request, user)
            return redirect('modulo_lider')






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
