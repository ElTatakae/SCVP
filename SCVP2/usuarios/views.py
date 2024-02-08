from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import CustomUserCreationForm
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@csrf_protect #Esto asegura que la validación del token CSRF se realice antes de procesar cualquier solicitud POST a esta vista.
def registro_de_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incio_lider')  # Redireccionar a una página de éxito
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro_de_usuario.html', {'form': form})

def inicio_panel(request):
    template = loader.get_template('inicio_panel.html')
    return HttpResponse(template.render())


def inicio_de_sesion(request):
    template = loader.get_template('inicio_de_sesion.html')
    return HttpResponse(template.render())

def base(request):
    template = loader.get_template('base.html')
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
