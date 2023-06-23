"""
instalar python

python -V

pip -V

pip install virtualenvwrapper
pip install virtualenv

--crear un entorno virtual
virtualenv nombre_entorno
virtualenv django_env

## Activando el entorno virtual

--powershell
.\django_env\Scripts\activate.ps1

--cmd
django_env\Scripts\activate.ps1

--onix
django_env/bin/activate

## Desactivar entorno virtual
deactivate


--si aparece el siguiente error, ejecutar los siguientes pasos

.\django_env\Scripts\activate.ps1 : File H:\Other computers\My computer\Edutecno Capacitacion\BOOTCAMP 0030 - FULL STACK PYTHON - VESPERTINO - 
workspace\M6-Django\2-S2\rebound\django_env\Scripts\activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at 
https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\django_env\Scripts\activate.ps1
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess

--obtener poliza de seguridad
Get-ExecutionPolicy

--desactivar la poliza de seguridad
Set-ExecutionPolicy RemoteSigned


--listar lista de paquetes instalados
pip list

--comandos de ayuda pip
pip help

--instalar django
pip install django

"""