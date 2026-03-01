#Creacion entorno virtual
    python -m venv .venv
#Se activa el entorno virtual
    .venv/Scripts/activate
#Se crea .gitignore

#Se instala django en el entorno virtual
    pip install django

#Se crea una carpeta llamada src(source)de codigo fuente

#Se accede a la carpeta src
    cd src

#Se ejecuta dentro de src
    django-admin startproject config .

#Para hacer funcionar el servidor
    python manage.py runserver

#En la linea 105 de config/settings.py se cambia el lenguaje a "es"

#En .gitignore se deben ignorar las carpetas __pycache__