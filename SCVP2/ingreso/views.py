from django.views.generic import TemplateView


class ingresoAdminView(TemplateView):
    template_name = 'ingreso_administrador.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class inicioView(TemplateView):
    template_name = 'inicio.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ingresoUsuarioView(TemplateView):
    template_name = 'ingreso_usuario.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
