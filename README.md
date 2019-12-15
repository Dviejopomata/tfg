# Proyecto fin de grado

## Python

Manejo de Fechas

Operaciones con colecciones

Testing

## Django

### Instalación

Relación de comandos de consola para crear un proyecto
django, una aplicación dentro de ese proyecto,
crear una base de datos sqlite (db.sqlite3) ylanzar el servidor

```console
django-admin startproject web
cd web
python .\manage.py startapp app1
python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py runserver
```
### Modelos


Capa de Negocio

Vistas

Forms
### Api
Para instalar el djangorestframework
```console
pip install djangorestframework
pip install markdown
pip install django-filter
```


## Celery
Instalación
```console
pip install celery
```
Si estamos en windows
```console
pip install eventlet
```

```python
from celery import Celery
app = Celery('tasks',
             broker='amqp://',
             backend='rpc://',
             )

# se define una tarea
@app.task
def add(x, y):
    return x + y

if __name__ == '__main__':
    app.start()
```
lanzar el proceso que conecta con el broker
en window hay que usar eventlet (pip install eventlet)
tasks se refiere al fichero tasks.py
definimos colas que luego podrán usarse en el cliente
```console
celery -A tasks worker -P eventlet -Q celery,priority.high --loglevel=info
```
codigo cliente para ejecutar codigo via workers
```python
from tasks import add
from celery import group
for i in range(1, 100):
    result=add.apply_async((i, i), )
    print(i, result.get())
```
Monitor de celery flower
```console
$ pip install flower
```



## Flutter

Instalación de Flutter

Creación de una aplicación

## CI/CD

Integración continua (git, pull request)

Continuous delivery.

