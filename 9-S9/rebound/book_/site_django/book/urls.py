from django.urls import path
from .views import IndexPageView, lista_libros, crear_libro, editar_libro, eliminar_libro, buscar_libro, registro, \
    iniciar_sesion, cerrar_sesion

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),  # registrando ruta
    path('lista_libros/', lista_libros, name='lista_libros'),  # registrando ruta para listar los libros
    path('crear_libro/', crear_libro, name='crear_libro'),  # registrando ruta para crear un libro
    path('editar_libro/<int:libro_id>', editar_libro, name='editar_libro'),  # registrando ruta para editar libro
    path('eliminar_libro/<int:libro_id>', eliminar_libro, name='eliminar_libro'),  # registrando ruta para eliminar libro
    path('buscar_libro', buscar_libro, name='buscar_libro'),  # registrando ruta para buscar libros
    path('registro/', registro, name='registro'),  # registrando ruta para registro de usuarios
    path('login/', iniciar_sesion, name='login'),
    path('logout/', cerrar_sesion, name='logout')
]
