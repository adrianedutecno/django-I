# create your forms
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Book


class BookForm(forms.ModelForm):
    #  estructuras para agregar validacion a valoración
    valoracion = forms.IntegerField(  # se sobreescribe del modelo el tipo de dato
        label='Valoración',  # label a mostrar en el input
        widget=forms.NumberInput(attrs={'class': 'form-control w-25'}),  # widgets de configuracion para los atributos del campo
        help_text='Valoración entre 0 y 100',  # texto de ayuda a mostrar, se sobreescribe del modelo
        validators=[MinValueValidator(0), MaxValueValidator(100)]  # validaciones para el campo o input de ingreso
    )

    class Meta:  # clase meta para establecer las caracteristicas del formulario BookForm
        model = Book  # modelo al que pertenece el formulario
        fields = ['titulo', 'autor', 'valoracion']  # campos que llevara el formulario
        labels = {
            'titulo': 'Titulo',  # el atributo del objeto es el key y el value es el label
            'autor': 'Autor'
        }
        widgets = {  # caracteristicas de los campos a mostrar en el formulario
            'titulo': forms.TextInput(attrs={'class': 'form-control w-100'}),
            'autor': forms.TextInput(attrs={'class': 'form-control w-100'}),
            # 'valoracion': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px'})
        }
