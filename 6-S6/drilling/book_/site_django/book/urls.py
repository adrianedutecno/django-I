from django.urls import path
from .views import IndexPageView, lista_libros, crear_libro

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),  # registrando ruta
    path('lista_libros/', lista_libros, name='lista_libros'),  # registrando ruta para listar los libros
    path('crear_libro/', crear_libro, name='crear_libro')  # registrando ruta para crear un libro
]
