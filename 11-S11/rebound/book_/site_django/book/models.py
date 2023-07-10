import datetime

from django.db import models


# Create your models here.
class Book(models.Model):
    titulo = models.CharField(max_length=100)  # titulo VARCHAR(100)
    autor = models.CharField(max_length=100)  # autor VARCHAR(100)
    valoracion = models.IntegerField(help_text='Valoración entre 0 y 100')  # valoracion INT
    fecha_creacion = models.DateTimeField(default=datetime.datetime.now)
    fecha_modificacion = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        permissions = [
            ('development', 'Permiso como Desarrollador'),
            ('scrum_master', 'Permiso como scrum_master'),
            ('product_owner', 'Permiso como Product_Owner')
        ]
