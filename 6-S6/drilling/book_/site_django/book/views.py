from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import BookForm
from .models import Book


# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'index.html'


# view o controlador para desplegar todos los libros
def lista_libros(request):
    libros = Book.objects.all()  # transaccion para obtener todos libros de la base de datos
    return render(request, 'lista_libros.html', {'libros': libros})


# view o controlador para crear libros
def crear_libro(request):
    if request.method == 'POST':  # si la peticion o request es de tipo post
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()  # transaccion para crear un registro de tipo libro en la base de datos
            return redirect('lista_libros')  # redirigiendo a la vista de listar libros si se crea el libro
    else:  # si la peticion no es de tipo post
        form = BookForm()  # establecemos el formulario a enviar y renderizar en la vista
        return render(request, 'crear_libro.html', {'form': form})  # se renderiza el template y se envia en el contexto el formulario
