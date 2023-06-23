'''
pip install virtualenv
pip install virtualenvwrapper

dentro de la carpeta a crear el entorno virtual
virtualenv nombre_entorno
virtualenv django_development
virtualenv django_development_1

-- activar entorno
.\nombre_entorno\Scripts\activate.ps1

nombre_entorno\Scripts\activate.ps1

source nombre_entorno/bin/activate

--desactivar
deactivate

--instalar paquete
pip install nombre_paquete
pip install django

--inicializar proyecto
pwd | para conocer en que carpeta nos encontramos
django-admin startproject nombre_proyecto
django-admin startproject project

ingresar a la primera carpeta del proyecto creado
cd nombre_proyecto
cd project

--inicializar aplicacion o app
django-admin startapp nombre_aplicacion
django-admin startapp app

'''

# registrar la aplicacion en el proyecto
# en el archivo settings.py
INSTALLED_APPS = [
    'app.apps.AppConfig',
    'app'
]