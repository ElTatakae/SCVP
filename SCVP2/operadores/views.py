from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def estadisticos(request):
    template = loader.get_template('estadisticos.html')
    return HttpResponse(template.render())


