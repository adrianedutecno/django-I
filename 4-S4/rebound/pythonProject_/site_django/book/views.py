from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("<h1>Bienvenidos a mi sitio de libros</h1>")
