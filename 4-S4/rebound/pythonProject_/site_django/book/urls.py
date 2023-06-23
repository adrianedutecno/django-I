from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')  # configuramos una url para el aplicativo que responde al path vacio
]
