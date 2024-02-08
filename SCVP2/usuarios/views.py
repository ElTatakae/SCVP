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

def agregar_grupo(request):
    template = loader.get_template('agregar_grupo.html')
    return HttpResponse(template.render())

def base(request):
    template = loader.get_template('panel.html')
    return HttpResponse(template.render())

def panel_lideres(request):
    template = loader.get_template('panel_lideres.html')
    return HttpResponse(template.render())

def panel_operadores(request):
    template = loader.get_template('panel_operadores.html')
    return HttpResponse(template.render())