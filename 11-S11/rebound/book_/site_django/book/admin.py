from django.contrib import admin

from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # configuracion read only
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_display = ('id', 'titulo', 'autor', 'valoracion', 'rating')
    list_filter = ('autor', 'valoracion', 'fecha_modificacion')

    @staticmethod
    def rating(obj):
        if obj.valoracion < 10:
            return 'Bajo'
        elif 10 <= obj.valoracion < 25:
            return 'Medio'
        else:
            return 'Alto'

    rating.short_description = 'Rating'


admin.site.register(Book, BookAdmin)  # registrar el modelo libro
