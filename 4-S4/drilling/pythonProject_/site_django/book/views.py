from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def index(request):  # forma para establecer un views o controlador mediante una funcion
    return HttpResponse("<h1>Bienvenidos a mi sitio de libros</h1>")


class IndexPageView(TemplateView):  # forma d utilizar una clase heredando desd TemplateView para renderizar un template
    template_name = 'index.html'




