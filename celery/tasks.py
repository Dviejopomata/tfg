from celery import Celery
# definición de la aplicación celery
app = Celery('tasks',
             broker='amqp://',
             backend='rpc://',
             )
# definicion de una tarea que se realizará
# cuando haya un mensaje en la cola
@app.task
def add(x, y):
    return x + y
# lanzamiento de la aplicación
if __name__ == '__main__':
    app.start()