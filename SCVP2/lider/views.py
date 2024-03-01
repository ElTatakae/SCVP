from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class InicioLiderView(LoginRequiredMixin, View):
    login_url ='/login/'
    redirect_field_name = '/login/'

    def get(self, request):
        return render(request, 'modulo_lider.html')


class crearGrupoView(TemplateView):
    template_name = 'grupo/crear_grupo.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class registroDeLideresYOperadoresView(TemplateView):
    template_name = 'registro/registro_usuarios.html'

    def post(self, request, *args, **kwargs):
        # Aquí va tu lógica para manejar la solicitud POST
        return super().get(request, *args, **kwargs)


class procesosView(TemplateView):
    template_name = 'proceso/procesos.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class productoView(TemplateView):
    template_name = 'producto/producto.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class monitoreoView(TemplateView):
    template_name = 'monitoreo/monitoreo.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class estadisticoView(TemplateView):
    template_name = 'estadistico/estadistico.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class asignarVariableView(TemplateView):
        template_name = 'producto/asignar_variable_producto.html'

        def post(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)


class asignarEstandarEquipoView(TemplateView):
    template_name = 'equipo/asignar_estandar_equipo.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class variableView(TemplateView):
    template_name = 'variable/variable.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
