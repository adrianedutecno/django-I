# agregar validacion para los views o controladores

# agregar views para home page not login

# Modificar modelo para agregar diferentes permisos

# Agregar permisos al usuario al momento de la creación

# permisos por usuario
from django.contrib.auth.models import User, Permission
usuario = User.objects.get(username='usuariotest')
usuario.get_all_permissions()

#permisos para un modelo en especifico
from book.models import Book
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
content_type=ContentType.objects.get_for_model(Book)
book_permissions=Permission.objects.filter(content_type=content_type)
[permiso.codename for permiso in book_permissions]

