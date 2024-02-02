from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .models import Empleado
from django.shortcuts import render, redirect
from .forms import InicioSesionForm
from django.contrib.auth import authenticate, login


'''
# Create your views here.
def inicioDeSesion(request):
    template = loader.get_template('ingreso.html')
    return HttpResponse(template.render())
'''


def inicioDeSesion(request):
    if request.method == 'POST':
        form = InicioSesionForm(request.POST)
        if form.is_valid():
            # Obtener datos del formulario
            numero_empleado = form.cleaned_data['numero_Empleado']
            contrasena_empleado = form.cleaned_data['contrasena_Empleado']

            # Autenticar al usuario utilizando la función authenticate de Django
            user = authenticate(request, numero_Empleado=numero_empleado, contrasena_Empleado=contrasena_empleado)

            if user is not None:
                # Iniciar sesión del usuario
                login(request, user)

                # Redirigir al usuario a la página deseada después de iniciar sesión
                return redirect('inicioAdministrador')
            else:
                # Si el usuario no existe o las credenciales son incorrectas, mostrar un mensaje de error
                messages.error(request, 'Credenciales incorrectas. Inténtalo de nuevo.')

    else:
        form = InicioSesionForm()

    return render(request, 'ingreso.html', {'form': form})


def registro(request):
    template = loader.get_template('registro.html')
    return HttpResponse(template.render())