from django.urls import path
from .views import IndexPageView, lista_libros

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),  # registrando ruta
    path('lista_libros/', lista_libros, name='lista_libros')  # registrando ruta para listar los libros
]
