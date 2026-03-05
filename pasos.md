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

#Para subirlo a github
    git add .
    git commit -m feat ...
    git push

#Para crear una aplicacion
    python manage.py startapp core

#Se debe registrar la app en settings.py

#Se creara la primera vista en views.py

#Se creara una puerta para ir a esa vista, en settings.py urls patterns
-------------------------------------------------------------------------------------asd

#Para ver que paquetes se tiene instalados en .venv
    pip freeze > requirements.txt

#Para reinstalar los paquetes
    pip install -r requirements.txt

#Para crear una funcion
    Se debe hacer una vista(funcion)
    Luego se debe registrar esa vista en config/urls.py

#Se debe crear la carpeta templates/core dentro de core
    Se creara un archivo index.html

#Git
#Para ver sobre que rama se esta parado
    git branch

#Para crear una nueva rama prueba
    git branch prueba

#Para cambiar a la rama prueba
    gir checkout prueba

    #Min 1 45

#Para unir lo de la rama prueba a rama main
    git merge prueba

#Se creara la aplicacion Producto
    python manage.py startapp producto

#Dentro de models, se creara una clase
    class


#Para crear la base de datos

    python manage.py makemigration

#Se debe invocar
    python manage.py migrate

#Para ver los datos de la db con Django, se creara una vista en producto/views.py
