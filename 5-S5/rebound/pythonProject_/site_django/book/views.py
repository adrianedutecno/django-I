from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def index(request):  # S3 forma para establecer un views o controlador mediante una funcion
    return HttpResponse("<h1>Bienvenidos a mi sitio de libros</h1>")


class IndexPageView(TemplateView):  # S4 forma d utilizar una clase heredando desd TemplateView para renderizar un template
    template_name = 'index.html'


def palindromo(request, palabra):  # S5 procesando palabra
    print(palabra)
    es_palindromo = "" #variable para acumular resultado y enviar a la vista

    #reemplazar espacios de la palabra por elementos vacios
    palabra_sin_espacio = palabra.replace(" ", "")  #yohagoyogahoy
    if palabra_sin_espacio == palabra_sin_espacio[::-1]:
        es_palindromo = "ES PALINDROMO"
    else:
        es_palindromo = "NO ES PALINDROMO"

    # setear datos en el context que viaja en el response
    context = {'es_palindromo': es_palindromo, 'palabra': palabra}
    #retornar a un template para renderizar los datos
    return render(request, 'espalindromo.html', context)
