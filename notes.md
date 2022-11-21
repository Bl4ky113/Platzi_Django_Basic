# Platzi: Django Básico

Un curso nuevo, de Pe a Pa, desde hace tanto tiempo. Dios.

Start: 11/18/2022
End: 

Sessions:
1. 11/18/2022 16:09 - ...
2. 11/20/2022 18:44 - ...
3. 11/21/2022 17:13 - 

## Introducción

El curso va a ser una instroducción básica a el Backend con Python de Django. 
Nuestro profesor va a ser Facundo García, grandioso profesor.
Requirements para el curso:
- Intro Backend
- Básico, Intermedio y Profesional de Python
- Git y Github
- OOP 
- Fundamentos de SQL
- Fundamentos de DBs Relacionales y No-Relacionales
- Programación Básica

Vamos a hacer un proyecto llamado Premios Platzi

## Que es Django

Es un framework que es buena base de grandes proyectos técnologicos Web.
Cómo Instagram, Pinteres, la App Web de Natgeo y Platzi. 
Es gratuito y Open Source, algunas caracteristicas son:
- Velocidad
- Seguridad
- Escabilidad
Es el 2do en el Top 3 de Frameworks para Apps Web en Python, Abajo de 
Flask, y arriba de FastAPI.

### Flask vs Django vs FastAPI
En sencillas descripciones:
- Flask: Versatíl, rápido de hacer y modular
- Django: Robusto y bastante completo
- FastAPI: Rápido y nuevo

## Instalación 

Vamos a usar una terminal, un editor de código y navegador web. 
Vamos a crear un venv de Python, installar django y sus requirements con Pip y listo.

Para hacer setup del proyecto, vamos a usar el cli django-admin así:

$ django-admin startproject nombre_proyecto

Esto nos creara una carpeta inicial con los archivos base de nuestro proyecto en Django.

## Archivos Base

Los archivos base que se crearon y creamos en la parte pasada, son la base para desarrollar nuestro
proyecto de Django

- .gitignore: 
    Lista de archivos que git va a ignorar.
- carpeta_proyecto/:
    Carpeta que contiene nuestro proyecto y sus archivos

Hay una cosa rara con Django, y es que en la carpeta de nuestro proyecto, crea un modulo de python
con el mismo nombre, puede ser confuso, pero meh.

Dentro de carpeta_proyecto:
- manage.py:
    Un script sencillo de python que nos permite ver y probar comando desde la terminal, donde 
    se ejecute el script.
- Modulo_Proyecto:
    Carpeta de un modulo del proyecto, que tiene el nombre de nuestro proyecto

Dentro de Modulo_proyecto:
- __init__.py
    El init del modulo
- asgi.py y wsgi.py:
    Archivos para poder hacer un Deploy de nuestro proyecto
- settings.py
    Configuraciones que vamos a poder hacer a nuestro proyecto. Cómo
    DBs y apps internos
- urls.py
    Son las direcciones que nuestro proyecto web va a tener

## El Servidor de Desarrollo

El Servidor de Desarrollo es una forma de poder crear y desarrollar nuestro proyecto backend sin 
tener que tener un servidor corriendo Django para probar y hacer debugging.
Además de agregarnos diferentes herramientas y cosas para que nosotros podamos hacer el desarrollo 
de mejor forma.

Para crear nuestro servidor de desarrollo, vamos a necesitar tener en nuestro proyecto_mod/settings.py 
tener nuestra variable DEBUG en True.
Vamos a ejecutar manage.py mandando el argumento runserver

$ python3 manage.py runserver

Esto hara que el servidor verifique los archivos y corra, haciendo un pequeño test 
en proyectos sin URLs en localhost puerto 8000

## Conceptos: App y Project

Un project va a ser el TODO de nuestro trabajo, ejemplo, 
Instagram en Django es el projecto, porqué es todo, con sus funcionalidades y APPs internas 
que hacen cómo diferentes módulos de funcionalidad. 
Siguendo este ejemplo, algunos sistemas DEBEN ir separados, cómo es el Feed y Mensajes privados, por ejemplo.
Estos sistemas se les considera cómo App en Django.

Platzi Awards va a ser nuestro Projecto. Y este va a tener de sistemas cómo el de polls

## Conceptos: Crear Apps y views en Nuestro Project

En nuestro project, vamos a usar diferentes apps, una de estas va a ser Polls. Y podemos hacer que Django nos
la creé usando manage.

$ python manage.py startapp app_name

Despues de esto, se creara el módulo, y App de Python, Django. 
En los archivos creados, que vamos a ver a lo largo del curso. 
Vamos a mirar views.py donde vamos a poder hacer diferentes views para nuestra app.

Para eso, vamos a importar de django.http HttpResponse. Y de ahí crear una app que 
reciba el method cómo parametro y retoner un HttpResponse.

Pero esta view no esta linkeada a nuestra app, ni a nuestro project. Para eso, vamos a 
ir al list urlpatterns en urls del modulo de nuestro poject. Vamos a crear un nuevo path, para 
nuestra app. 
Generalmente 'polls/', y esta url se va a importar de polls.urls, usando include:

urlpatterns = [
    path('polls/', include('polls.urls'))
]

Cómo este archivo no existe, vamos a crearlo. Y para eso simplemente, vamos a seguir la misma 
estructura de project.urls
Importamos path de django.urls y importamos las views de nuestra app para conectarla haciendo paths 
en una lista urlparametters. Pero lo extra, es que en path podemos agregar un parametro name, para 
ponerle nombre al path de la url de nuestra view.

##
