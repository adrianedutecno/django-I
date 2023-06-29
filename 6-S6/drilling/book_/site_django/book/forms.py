# create your forms
from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:  # clase meta para establecer las caracteristicas del formulario BookForm
        model = Book  # modelo al que pertenece el formulario
        fields = ['titulo', 'autor', 'valoracion']  # campos que llevara el formulario
        widgets = {  # caracteristicas de los campos a mostrar en el formulario
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'autor': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'valoracion': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px'})
        }
