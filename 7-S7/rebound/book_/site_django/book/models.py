from django.db import models


# Create your models here.
class Book(models.Model):
    titulo = models.CharField(max_length=100)  # titulo VARCHAR(100)
    autor = models.CharField(max_length=100)  # autor VARCHAR(100)
    valoracion = models.IntegerField(help_text='Valoración entre 0 y 100')  # valoracion INT
