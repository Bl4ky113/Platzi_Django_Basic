# Curso de Django Intermedio 

Ahora vamos a terminar de una con toda. Mismo sistema

start: 12/17/2022
end: NEVER

Malparidos!!! Me hicieron volver a VSC!!! Pero bueno, recuerdo alguna que otra cosita.
Las Notas se seguiran tomando por acá

## Que son los Tests en Django?

Los Tests de Django, es una funcion que verifica que nuestro código funcione correctamente. Esto es más que todo 
para que nuestros projectos puedan escalar de una mejor forma. Tanto en el presente, pasado y futuro.

Esto ademas de crecimiento, ayuda con la estabilidad de cambios. De personal, de tecnologías y demás.
Lo mejor es plantear primero la idea o forma del negocio y realizar un desarrollo TDD.

Para hacer tests vamos a ir al archivo test de nuestra app. Generalmente en Django se hacen tests de Models u 
de Views, aunque para funciones complejas de nuestra app, tambien se pueden hacer tests.

Vamos a crear una clase que herede de django.test TestCase. Para tener las habilidades de testing en Django.
dentro de está, vamos a crear una funcion que inicie por test_ donde vamos a hacer nuestros tests. 
Para verificar, o lanzar error si hay algo mal, vamos a usar self.assert functions. Las cuales 
generalmente toman 2 u varios valores para verificar su función lógica, la más sencilla es igualdad
o assertIs, donde verifica que un dato sea otro.

Para ejecutar estos test, vamos a usar el manage.py tests y el nombre de la app.

$python3 manage.py test app

Estos se ejecutaran y daran reporte de los errores. Al ejecutarse se generará un ambiente de 
testing, creando y aislando la db de nuestra app con la del testing.

### Tips con los Test
Cómo nuestros tests van a ir creciendo cada vez que vayamos implementado cosas, vamos a algunas veces 
repetir una misma forma de iniciar los tests u de terminarlos. 
Para evitar este DRY, vamos a poder crear una funcion setUp() y tearDown(). Donde se ejecutara al inicio 
y final de cada test.

Algunas veces los Assert van a tener que ser especiales, cómo con ejemplo los Queries set.

## Testing Views

Para testear views, vamos a poder usar dentro de una clase heredada de TestCase, podemos usar 
self.client.get() y la url de nuestra app u view para hacer diferentes cosas.
Podemos obtener la response guardando el return de esa function. Y desde ahí se puede acceder:
- El número / tipo de respuesta
- General respuesta http
- Contenidos del Context, cómo si fuera un dict.

Ademas de generalmente crear varios tests, se pueden crear 
varias iteraciones de un mismo test, pero para simplemetne cambiar el número de capacidad?
Eso se le conoce como covertura.

No alcance a terminar el curso :( Talvez lo hubiera terminado completo si fuera hasta las 12 PM
