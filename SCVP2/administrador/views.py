from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import registroAdministradorForm, ingresoAdminForm
#from django.views.decorators.csrf import csrf_protect
#from django.views.decorators.csrf import csrf_exempt


#@csrf_exempt
#@csrf_protect #Esto asegura que la validación del token CSRF se realice antes de procesar cualquier solicitud POST a esta vista.
def registro_de_usuario(request):
    template = loader.get_template('registro/registro_de_usuario.html')
    return HttpResponse(template.render())

def inicio_panel(request):
    template = loader.get_template('inicio_panel.html')
    return HttpResponse(template.render())
def registro_de_administrador(request):
    template = loader.get_template('registro/registro_de_administrador.html')
    return HttpResponse(template.render())


def inicio_de_sesion(request):
    template = loader.get_template('inicio_de_sesion.html')
    return HttpResponse(template.render())

def panel_administrador(request):
    template = loader.get_template('panel_administrador.html')
    return HttpResponse(template.render())

def modulo_lider(request):
    template = loader.get_template('modulo_lider.html')
    return HttpResponse(template.render())

def modulo_administrador(request):
    template = loader.get_template('modulo_administrador.html')
    return HttpResponse(template.render())

def modulo_operador(request):
    template = loader.get_template('modulo_operador.html')
    return HttpResponse(template.render())

def inicio(request):
    template = loader.get_template('landingpage.html')
    return HttpResponse(template.render())

def registro_de_empresa(request):
    template = loader.get_template('registro/registro_de_empresa.html')
    return HttpResponse(template.render())



def registro_administrador(request):
    if request.method == 'POST':
        form = registroAdministradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio_sesion')  # Redirige al inicio de sesión después del registro exitoso
    else:
        form = registroAdministradorForm()
    return render(request, 'registro_administrador.html', {'form': form})

def ingreso_administrador(request):
    if request.method == 'POST':
        form = ingresoAdminForm(request.POST)
        if form.is_valid():
            numero_empleado = form.cleaned_data['numero_empleado']
            contrasena = form.cleaned_data['contrasena']
            user = authenticate(request, numero_empleado=numero_empleado, contrasena=contrasena)
            if user is not None:
                login(request, user)
                return redirect('modulo_administrador')  # Redirige al panel de control después del inicio de sesión exitoso
            else:
                # Mensaje de error si las credenciales son inválidas
                messages.error(request, 'Número de empleado o contraseña incorrectos.')
    else:
        form = ingresoAdminForm()
    return render(request, 'ingreso_administrador.html', {'form': form})

