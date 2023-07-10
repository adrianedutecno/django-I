import datetime
import logging

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import TemplateView

from .forms import BookForm
from .models import Book


# Create your views here.
class IndexPageView(TemplateView):
    template_name = 'index.html'


# view o controlador para desplegar todos los libros
@login_required
def lista_libros(request):
    libros = Book.objects.all()  # transaccion para obtener todos libros de la base de datos
    return render(request, 'lista_libros.html', {'libros': libros})


# view o controlador para crear libros
@login_required
def crear_libro(request):
    if request.method == 'POST':  # si la peticion o request es de tipo post
        form = BookForm(request.POST)
        if form.is_valid():  # si el formulario es valido
            form.save()  # transaccion para crear un registro de tipo libro en la base de datos
            messages.success(request, 'Libro agregado éxitosamente')  # mensaje de exito
            return redirect('lista_libros')  # redirigiendo a la vista de listar libros si se crea el libro
        else:  # si el formulario no es valido, no cumple las validaciones
            messages.error(request, 'Módifica los datos de ingreso')  # crear mensaje de error para enviarla a la vista
            return HttpResponseRedirect(reverse('crear_libro'))
    else:  # si la peticion no es de tipo post
        form = BookForm()  # establecemos el formulario a enviar y renderizar en la vista
        return render(request, 'crear_libro.html',
                      {'form': form})  # se renderiza el template y se envia en el contexto el formulario


# view o controlador para editar libros
@login_required
def editar_libro(request, libro_id):
    book = get_object_or_404(Book, id=libro_id)  # obtener libro en la db mediante el id
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)  # guardamos en memoria se rescata el libro
            book.fecha_modificacion = datetime.datetime.now()  # fecha_modificacion
            book.save()  # guardamos el libro
            messages.success(request, 'Libro editado éxitosamente')
            return redirect('lista_libros')
        else:
            messages.error(request, 'Módifica los datos de ingreso')
            return HttpResponseRedirect(reverse('editar_libro', args=[libro_id]))
    else:
        form = BookForm(instance=book)
        return render(request, 'editar_libro.html', {'form': form, 'libro_id': libro_id})


# view o controlador para eliminar libros
@login_required
def eliminar_libro(request, libro_id):
    book = get_object_or_404(Book, id=libro_id)  # obtener libro en la db mediante el id o error 404
    # book = Book.objects.get(id=libro_id)
    book.delete()  # elimina el libro encontrado de la base de datos
    messages.info(request, 'Libro eliminado éxitosamente')
    return redirect('lista_libros')


# view o controlador para buscar libros
@login_required
def buscar_libro(request):
    if request.method == 'GET':
        query = request.GET.get('query')  # obteniendo el name='query' agregado al input en form del navbar
        libros = Book.objects.filter(Q(titulo__icontains=query) | Q(autor__icontains=query))
        return render(request, 'buscar_libro.html', {'libros': libros})


# view o controlador para el registro
def registro(request):
    if request.method == 'POST':  # se valida la peticion de tipo post
        form = UserCreationForm(request.POST)  # se crea el formulario basado en el request.POST
        if form.is_valid():  # si el formalurio es valido
            user = form.save()  # se guarda el usuario registrado

            # agregando permisos
            content_type = ContentType.objects.get_for_model(Book)
            permission = Permission.objects.get(
                codename="development",
                content_type=content_type,
            )
            user.user_permissions.add(permission)

            messages.success(request, 'Registrado éxitosamente')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


# view o controlador para el iniciar sesion
def iniciar_sesion(request):
    if request.method == 'POST':  # si el request es de tipo post
        username = request.POST['username']  # captura username del request
        password = request.POST['password']  # captura password del request
        user = authenticate(request, username=username, password=password)  # se captura el usuario encontrado
        if user is not None:  # si el usuario autenticado no viene vacio, quiere decir es validas sus credenciales
            login(request, user)
            return redirect('lista_libros')
        else:
            messages.error(request, 'Credenciales inválidas')
            return render(request, 'login.html')
    return render(request, 'login.html')  # tipo get


# view o controlador para cerrar sesion
def cerrar_sesion(request):
    logout(request)  # se deslogue
    return render(request, 'login.html')


# view o controlador para home page not login
def home_page_not_login(request):
    return render(request, 'index.html')





