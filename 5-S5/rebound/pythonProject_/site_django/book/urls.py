from django.urls import path
from .views import IndexPageView, palindromo
from . import views

urlpatterns = [
    # path('', views.index, name='index')  # configuramos una url para el aplicativo que responde al path vacio
    path('', IndexPageView.as_view(), name='index'),
    path('palindromo/<str:palabra>', palindromo, name='palindromo')
]
