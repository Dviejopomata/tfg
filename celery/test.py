from tasks import add
from celery import group
# se lanzar 100 tareas
for i in range(1, 100):
    result=add.apply_async((i, i), )
    print(i, result.get())
# se lanzan 4 tareas dentro de un grupo
numbers = [(2, 2), (4, 4), (8, 8), (16, 16)]
res = group(add.s(i, j) for i, j in numbers).apply_async(queue='priority.high', serializer="json")
# aquí tenemos el resultado de las tareas
print(res.get())