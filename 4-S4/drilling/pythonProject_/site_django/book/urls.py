from django.urls import path
from .views import IndexPageView
from . import views

urlpatterns = [
    # path('', views.index, name='index')  # configuramos una url para el aplicativo que responde al path vacio
    path('', IndexPageView.as_view(), name='index')
]
