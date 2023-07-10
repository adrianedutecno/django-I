# Habilitar los campos fecha_creacion y fecha_modificacion,
# y que sean de solo lectura al visualizar un determinado libro.
    # book/admin.py
    class BookAdmin(admin.ModelAdmin):
        # configuracion read only
        readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    admin.site.register(Book, BookAdmin)  # registrar el modelo libro


# Visualizar el título, valor y valoración respectivamente.
    # book/admin.py
    class BookAdmin(admin.ModelAdmin):
    # configuracion read only
        readonly_fields = ('fecha_creacion', 'fecha_modificacion')
        list_display = ('id', 'titulo', 'autor', 'valoracion')

# Agregar un filtro según la valoración, y la fecha de modificación.
    # book/admin.py
    class BookAdmin(admin.ModelAdmin):
    # configuracion read only
        readonly_fields = ('fecha_creacion', 'fecha_modificacion')
        list_display = ('id', 'titulo', 'autor', 'valoracion')
        list_filter = ('valoracion', 'fecha_modificacion')