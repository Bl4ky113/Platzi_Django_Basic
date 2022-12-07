# Platzi: Django Básico

Un curso nuevo, de Pe a Pa, desde hace tanto tiempo. Dios.

Start: 11/18/2022
End: 

Sessions:
01. 11/18/2022 16:09 - ...
02. 11/20/2022 18:44 - ...
03. 11/21/2022 17:13 - ...
04. 11/22/2022 16:53 - 18:09
05. 11/24/2022 14:36 - ...
06. 11/26/2022 20:22 - 21:19
07. 11/27/2022 18:26 - ...
08. 11/28/2022 14:40 - 18:15
09. 11/29/2022 12:30 - ...
10. 12/01/2022 18:48 - ...
11. 12/05/2022 15:31 - 22:20
12. 12/06/2022 14:11 - 

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

$ django-admin startproject nombre\_proyecto

Esto nos creara una carpeta inicial con los archivos base de nuestro proyecto en Django.

## Archivos Base

Los archivos base que se crearon y creamos en la parte pasada, son la base para desarrollar nuestro
proyecto de Django

- .gitignore: 
    Lista de archivos que git va a ignorar.
- carpeta\_proyecto/:
    Carpeta que contiene nuestro proyecto y sus archivos

Hay una cosa rara con Django, y es que en la carpeta de nuestro proyecto, crea un modulo de python
con el mismo nombre, puede ser confuso, pero meh.

Dentro de carpeta\_proyecto:
- manage.py:
    Un script sencillo de python que nos permite ver y probar comando desde la terminal, donde 
    se ejecute el script.
- Modulo\_Proyecto:
    Carpeta de un modulo del proyecto, que tiene el nombre de nuestro proyecto

Dentro de Modulo\_proyecto:
- \_\_init\_\_.py
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

Para crear nuestro servidor de desarrollo, vamos a necesitar tener en nuestro proyecto\_mod/settings.py 
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

$ python manage.py startapp app\_name

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

## Investigación Settings.py

En la clase cómo tal es bastante básica y vacia, solo nos explica 3:
- TIME\_ZONE: Simplemente el Time zone en el que Django cree que esta. Se puede cambiar 
    de UTC a el de nuestra ciudad u pais, pero toca buscarlo.
- INSTALLED\_APPS: Las apps instaladas en nuestro projecto, aunque al parecer toca agregar 
    las apps creadas por uno mismo como Polls
- DATABASES: Es dict que parece lista, de DBs, generalmente solo se 
    usan DBs relacionales con Django, y para usar No-Relacionales, toca 
    hacer maromas u algo. Estas pueden tener diferentes formas de configuración
    como tener usuario y password. La Default es SQLite3
- MIDDLEWARE: Es simplemente un puente sencillo y muy rápido entre algunas apps y procesos de Django.

### Tip manejar Middleware y Apps de Django
Para hacer este proceso y instalación más sencillo, simplemente vamos a 
quitar o renombrar INSTALLED\_APPS & MIDDLEWARE, a DJANGO\_APPS & DJANGO\_MIDDLEWARE.
Esto para crear nuestras propios tuples con nuestras apps y middleware, o inclusive crear 
una tercera lista para terceros. Y despues vamos a definir que INSTALLED\_APPS es igual a 
la suma de todas las listas, lo mismo con el MIDDLEWARE.

INSTALLED\_APPS = DJANGO\_APPS + LOCAL\_APPS + THIRD\_PARTY\_APPS

Ya vere otras configs más adelante

## Que es un ORM?

Un Oject Relational Mapping es la forma en la que usando OOP vamos a crear una DB Relacional. 
Estas principalmente se crean un sistema de relaciones de cada elemento de la DB con uno de OOP.
- Tabla -> Script
- Row -> Class 
- Column -> Attribute

Los objects creados se pueden pasar a la DB relacional sin problema.

Podemos simplemente esquematizar las tablas de nuestra DB y por lo tanto las Classes que vamos a 
crear. Simplemente hacemos una lista de los valores que se van a necesitar, y si necesitamos 
podríamos hacer abstracción de nuestras tablas. Para evitar repetir espacios. 

En el curso se recomienda tener dos tablas, una de preguntas y otra de respuestas para estas preguntas.
Siendo 1:n respectivamente.

Los datos de las tablas son:

### Questions
- ID
- question
- date

### Answers
- ID
- Question\_ID
- answer
- answer\_count

## Crear un ORM, Models y demás en Django.

Vamos a ir a Models de nuestra app, polls en nuestro caso. Vamos 
a crear un model con una class partiendo desde models.Models de django.db. 

Y para definir los tipos de valores & columnas del Model, vamos a crear 
atributos a nuestra clase. Usando como tipo de valores clases de valores 
de nuestra DB, en este caso SQLite. Los cuales simplemente los podemos encontrar 
en models cómo "tipo\_de\_dato"Field(), y podemos pasarle parametros para este valor, cómo
largo máximo con str. O el mismo nombre del Field. Estos parametros nos pueden dar funcionalidades 
más especificas, cómo el que hacer cuando se elimine una llave foranea de un elemento,

Pero ahora que tenemos nuestros models, debemos simplemente hacer otros pasos que nos falto hacer.


### Agregar una App a Django
Hemos creado una app desde la terminal, le agregamos una view y ahora unos models para nuestra db. Pero 
cómo tal Django no tiene agregada esta App, esto es bastante sencillo, simplemente podemos agregar nuestra
app en la lista de INSTALLED\_APPS. Ya sea al inicio o al final, u usando la tecnica y truco anteriormente dicho.


Listo, ahora vamos a usar el script manage.py para ejecutar 2 comandos:

$ python3 manage.py makemigrations polls

Lo primero que vamos a hacer acá es que Django va a tomar los models de nuestra app polls, y va a 
crear un script en los cuales va a crear en la DB las tablas con las propiedades dadas por los Models.

y

$ python3 manage.py migrate

Va a ejecutar en nuestra DB los scripts de migrations creados, esto principalmente para tener un registro 
de lo realizado en la DB.

Nos habra salido bien los comandos si, se crearon migraciones para Polls y al migrar estas se obtiene OK en todo

## Consola de Django

Como la consola interactiva de Python, la cual podemos ingresar usando $ python3. Podemos 
ingresar y usar una terminal shell de nuestro proyecto en Django, usando:

$ python3 manage.py shell

Desde esta podemos interactuar con nuestro project de una forma más directa. Escencialmente 
podemos mirar, hacer queries, crear datos y demas con los modelos en nuestra DB.
Creo que es un poco más que obvio que podemos automatizar cada cosa que hagamos en la 
consola usando código, solo sería ver donde y que implementar exactamente.

Para hacer queries podemos importar los modelos de polls.models. Y usando un methodo static de 
los modelos, objects, podemos hacer queries a la DB. El más sencillo, de todos los valores es 

Model.objects.all() : Que trae todos los datos.

Para guardar un dato, vamos a crear una instancia del Model. Y los valores de este los vamos a pasar cómo 
un karg.

Despues de esto, vamos a usar el metodo save() de la instancia para que los valores se guarden correctamente 
en la DB.

value = Model(value=value)
value.save()

Esta instancia vamos a poder acceder a sus valores, como si fueran atributos normales de una clase.
Pero al momento de imprimirla con un print(). Nos va a salir el tipo de dato que es, el Model.
Para arreglar esto parcialmente, podemos agregar un method \_\_str\_\_ a nuestro model. 
Este simplemente va a retornar un string de lo que debería representar nuestro model, ejecutandose 
cada vez que python necesite que estas instancias sean strings. Ya sea para imprimir.

### Metodos Personalizados para Models
Simplemente vamos a crear un method como si fuera una class normal de python.

## Queries desde Consola

Para hacer queries sencillos, podemos usar Model.objects.get(), este no lo 
podemos usar cómo all(), ya que debe retornar solo un object. 
Una forma sencilla es buscar usando primary keys, o "pk", 
que practicamente van en orden ascendente desde 1 hasta el ultimo valor 
de la db. 

Se pueden hacer queries un poco más complejos usando operadores especiales de las 
propiedades de nuestra DB, aunque ojo, al usar get(), puede que nos de error al 
tener más de un object con las caracteristicas del query. 
Estos operadores se aplican de una forma particular, se debe escribir un 
downder y luego el operador, despues de escribir la propiedad a la que se le 
va a aplicar. Ejemplo:

publication\_day\_\_operador=rango\_valores\_operador

Podemos obtener varios elementos en una lista usando Models.objects.filter()
es básicamente el mismo proceso que .get()

### Lista Operadores Query 
- exact="": match exacto
- iexact="": match exacto, con case sensitive
- contains="": match
- icontains="": match, ...
- in=[], in="": check si esta en un iterable
- gt=0: greater than
- gte=0: greater equal
- lt=0: less than
- lte=0: less equal than
- startswith="": match en el inicio
- istartswith="": match ..., ...
- endswith="": match en el final
- iendswith="": ... ..., ...
- Un tretamonton de operadores para fechas, horas y formatos de estas
- regex="": regex
- iregex="": ...
- isnull=Bool: Mira si es null o no
Se pueden combinar varios de estos operadores, sobretodo los de fecha con lo lógicos generales: gt lt.

Ademas de estos operadores, si en nuestro modelo tenemos una foreign key. Podemos acceder a los valores
de esos datos usando \_\_valor, y inclusive podemos agregarle a estos valores otros operadores, para 
hacer queries.

## Conjunto de Datos Relacionados

Los Datos Relacionados son aquellos que se pueden expresar cómo relaciones de tablas, 1:1, 1:n, n:n*. 
Estas relaciones generalmente se pueden acceder desde el modelo principal o que se vaya a usar, 
usando el nombre del modelo relacionado, junto a \_set. Y desde ahí se pueden hacer diferentes cosas 
en el modelo relacionado, cómo crear, buscar, eliminar, entre otros los datos.

Acceder a estos datos puede ser más sencillo, en el momento de crear el dato de Foreing key en el Modelo Relacionado.
Vamos a pasar un karg de related\_name="", donde vamos a pasar el nombre de la relación del modelo principal y el 
relacionado. Esto para evitar usar siempre el model\_set que se genera automaticamente, y usar algo más descriptivo. 

Además de lo methods ya vistos, podemos hacer un .count() para contar cuantos elementos relacionados 
del Model Relacionado tenemos.

## Django Admin

Es un super usuario que nos va a poder permitir administrar datos de nuestra DB, 
pero de una forma más visual y sencilla, que desde la terminal.
Pero para esto se puede crear usando $ python3 manage.py createsuperuser.

Donde simplemente nos va a pedir un nombre de usuario, email y contraseña. 
Pero primero, para hacer funcional nuestro usuario admin, debemos primero registar 
en nuestra app admin.py los Models que vayamos a usar.

Esto simplemente se usa el modulo admin, propiedad site y method register, al cual 
pasamos los modelos a usar. Los cuales deben ser importados.

Ya despues de tener nuestro usuario, vamos a poder accederlo desde localhost:8000/admin/ 
por default, puede cambiar si cambiamos el puerto o el url de admin que esta por default en urls.py 
de la app de nuestro proyecto.

Usandolo por un rato, parece ser solo una interfaz grafica para modificar y ver datos de los modelos del proyecto,
que se hayan pasado al admin, ya que no todos los modelos estan por defecto. Solo los 
que estan por defecto son los de Grupos y Usuarios en el project. 
Se pueden dar permisos a grupos u usuarios, operaciones crud sencillas y demás.

## MTV

En Django se usa un sistema de MTV:
- M: Models
- T: Templates
- V: Views

Models, ya los hemos visto. Pero Templates y Views, solo superficie. 
Las Views es la forma en la que se va a poder interactuar, tanto visual pasando 
datos y demás cosas para visualizar, cómo recibir datos de un formulario.
Las Templates, son la forma en la que las Views van a ser representadas, 
generalmente cómo un archivo HTML5, con algunas adiciones de Django.

Las views pueden ser dividas entre hechas por funciones o clases. 
Funcion Based View y Generic View, respectivamente. Las diferencias 
las veremos en otra clase.

Esto es con MTV, haciendo que el Backend y el Frontend sean desarrollados por 
las mismas personas o cómo minimo en el mismo framework, Django.
Para usar otras formas de desarrollo Frontend, lo vamos a ver en el curso.

## Agregar Views PT 2

Para agregar Views, simplemente vamos a ir al archivo views.py de nuestra app. Crear la function o class de 
la view, que siempre retorne un elemento, generalmente un httpresponce(). A

Desde ahí vamos a importar el archivo de views a nuestro archivo de urls.py y vamos a agregar a la lista de 
urlpatterns los paths de nuestras views.
En el path podemos agregar variables atravez de nuestra url, al usar \<tipo_variable:nombre_variable\>. Generalmente
solo se pueden usar int, y strs. Pero para usar estas variables, las vamos a tener que definir en nuestra function o class 
view cómo un parametro, usando el mismo nombre que nombre_variable.

## Templates en Django

Las Templates son el Frontend que va a tener nuestras Views. Esto lo vamos a definir 
en archivos separados en una carpeta llamada templates, una por app.
Cómo es una carpeta por app, lo mejor es hacer un subfolder de nuestra app, aunque quede feo.
Para evitar que al momento de que Django combine las templates, pueden haber errores de archivos 
duplicados en diferentes apps.

Resumido, mejor tener esta estructura:
project/
    app/
        templates/
            app/
                template_1
                templates...
    app_2
        templates/
            app_2/
                template_1

Si no hubieramos tenido los templates_1 en diferentes carpetas dentro templates. Django hubiera dado error.

Pero ya en la template que vayamos a usar, vamos a poder crear un archivo html normal, con 
unos agregados:
- Bloques de código {% %}
- Inssert de Variable en el Html {{ }}

Dentro de los Bloques de Código vamos a poder usar if, else, for y sus finalizadores endif-for
Para agregar un sistema de lógica a nuestro template. Exactamente cómo si fuera una Jinja Template

## Levantar Errores HTTP

Podemos usar diferente metodos para levantar errores http en Django, pero uno util es cuando 
necesitamos buscar algo en nuestra db y al no encontrarlo, devolver 404. Esto Django tiene un shotcut 
integrado para evitar hacer toda una estructura de manejo del error al no encontrar el dato de la db.

No, simplemente vamos a importar de django.shortcuts get_object_or_404 que literalmente hace lo que dice. Solo 
necesita el modelo de la db a la cual se va a buscar y los kwargs del filter.

## Evitar el Hard Coding de URLs

El Hard Coding es la mala practica de hacer que nuestras URLS de nuestro project sean 
siempre iguales frente una viriable, esto puede ser inocente al incio, ejemplo. 
Simplemente nombrar el módulo polls/ y para cada view de nuestro modulo poner 
polls al inicio. Esto esta bien hasta que polls cambia de nombre y se daña todo 
el módulo.
 
Para evitar esto simplemente vamos a usar en la jinja template, url 'nombre_modulo:nombre_view' parametros_url ...
Pero ojo, el nombre lo tenemos que definir en urls de nuestro modulo cómo una vairable global que 
Django va a leer llamada, app_name. Y los nombre views, van a ser los name="" que estan en el path de urlpatterns.

Ojo que al parecer el name="" y el nombre de la view cómo tal pueden confundir al metodo de url.
