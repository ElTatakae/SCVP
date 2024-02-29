from django.views.generic import TemplateView


class adminInicioView(TemplateView):
    template_name = 'modulo_administrador.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class registroEmpresaView(TemplateView):
    template_name = 'registro/registro_de_empresa.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class registroLiderView(TemplateView):
        template_name = 'registro/registro_de_lideres.html'

        def post(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)


class registroAdminView(TemplateView):
    template_name = 'registro/registro_de_administrador.html'

    def post(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


