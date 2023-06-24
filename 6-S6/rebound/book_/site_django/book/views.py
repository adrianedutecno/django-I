from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Book


# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'index.html'


# view o controlador para desplegar todos los libros
def lista_libros(request):
    libros = Book.objects.all()  # transaccion para obtener todos libros de la base de datos
    return render(request, 'lista_libros.html', {'libros': libros})
