from django.shortcuts import render
from django.http import HttpResponse
from app1.tasks import add
from web.celery import debug_task
import random
# Create your views here.
def post_list(request):
     a = random.randint(1, 10)
     b = random.randint(1, 10)
     c = f"{a} {b} {add.apply_async((a, b)).get()}"
     return HttpResponse(c )