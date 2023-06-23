'''
--listando paquetes
pip list

--instalando django en el entorno virtual
pip install django

--actualizar pip
python.exe -m pip install upgrade pip

--inicializar proyecto
django-admin startproject site_django

--ir a la carpeta creada en la terminal
cd site_django

--inicializar la aplicacion llamada book
django-admin startapp book
'''

'''
--agregar en installed app la aplicacion en settings del proyecto
dentro de site_django
'''
INSTALLED_APPS = [
        'book.apps.BookConfig',  # agregando app al registro de aplicaciones instaladas en el proyecto
]

'''
--configuraciones iniciales para base de datos y autentificación

python manage.py migrate
'''

'''
python manage.py runserver

ir luego a la url en el navegador: http://127.0.0.1:8000/


ctrl + c para salir del servidor o kill
'''

'''
python manage.py help comando
ej: python manage.py help makemigrations

makemigrations: Este comando es utilizado para crear archivos de migración en Django. Las migraciones son archivos que contienen cambios en el esquema de la base de datos, como la creación de nuevas tablas o la modificación de las existentes. El comando makemigrations analiza los modelos definidos en tu proyecto y genera los archivos de migración correspondientes que luego podrán ser aplicados a la base de datos.

migrate: El comando migrate se encarga de aplicar las migraciones a la base de datos. Ejecuta los archivos de migración pendientes en el orden adecuado para asegurar que la estructura de la base de datos esté sincronizada con los modelos definidos en tu proyecto.

shell: Este comando inicia una sesión interactiva de Django shell. Proporciona una interfaz de línea de comandos para interactuar con tu proyecto Django. Puedes ejecutar consultas de base de datos, crear, modificar o eliminar objetos, realizar pruebas, entre otras tareas.

dbshell: El comando dbshell inicia una consola interactiva de la base de datos. Te permite acceder directamente a la línea de comandos de tu base de datos, lo que puede ser útil para ejecutar consultas SQL personalizadas o realizar tareas específicas directamente en la base de datos.

showmigrations: Este comando muestra el estado de las migraciones en tu proyecto. Indica qué migraciones han sido aplicadas y cuáles están pendientes de aplicación. Puedes utilizarlo para verificar el estado de las migraciones y asegurarte de que todo esté sincronizado correctamente.

dumpdata: El comando dumpdata se utiliza para exportar los datos de la base de datos en formato JSON o YAML. Puedes especificar qué modelos o aplicaciones deseas incluir en la exportación. Es útil para realizar copias de seguridad de los datos o para transferirlos entre diferentes entornos.

test: Este comando se utiliza para ejecutar las pruebas unitarias en tu proyecto. Ejecuta todas las pruebas definidas en los archivos tests.py de tus aplicaciones y muestra los resultados en la consola.

testserver: El comando testserver inicia un servidor de desarrollo con una copia de la base de datos en memoria y cargando datos de prueba. Es útil para ejecutar pruebas que requieren acceso a una base de datos y datos específicos.

diffsettings: Este comando muestra las diferencias entre los archivos de configuración de Django (settings.py) y la configuración actual de tu proyecto. Puedes utilizarlo para ver los cambios realizados en la configuración o para solucionar problemas relacionados con la configuración de tu proyecto.
'''