# crear un super usuario
    #ejecutar en la carpeta que contiene el manage.py
python manage.py createsuperuser
'''
Nombre de usuario (leave blank to use 'adria'): superuser
Dirección de correo electrónico: superuser@gmail.com
Password:
Password (again):
La contraseña es demasiado similar a la de nombre de usuario.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

'''

# verficar el registro del sitio administrativo
# proyecto/urls.py

# ingresar al sitio administrativo con el superuser
# levantar el proyecto
    # en la terminal:
    python manage.py runserver
    # ruta para ingresar al sitio administrativo
    127.0.0.1:8000/admin

# Registrar la aplicación Book en el sitio administrativo de Django.

# Configurar con la finalidad de que el sitio administrativo aparezca como Libro y Libros,
# respectivamente.
    #agregar a book/apps.py
    verbose_name = 'Libro'
    #agregar a book/models.py en class Meta:
    verbose_name = 'Libro'
    verbose_name_plural = 'libros'
    #aplicar migraciones
    python manage.py makemigrations
    python manage.py migrate
    #ejecutar aplicativo
    python manage.py runserver

# Agregar dos atributos especiales al modelo del tipo fecha: uno que se refiere a la fecha de creación
# (fecha_creacion), y el otro a la fecha de modificación (fecha_modificacion).
    #aplicar migraciones
    python manage.py makemigrations
    python manage.py migrate
    #ejecutar aplicativo
    python manage.py runserver