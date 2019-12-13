from celery import task


@task
def add(x, y):
    print('add')
    return x + y


@task
def mul(x, y):
    return x * y


@task
def xsum(numbers):
    return sum(numbers)