"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/',     path('cliente_list', ClienteListView.as_view(), name='list_clientes'),
include('blog.urls'))
"""

import eventlet
eventlet.monkey_patch()
from django.contrib import admin
from django.urls import path, include
from app1.views import EjemploTemplateView, DireccionView, ClienteCreateView, ClienteListView, ClienteUpdateView, ClienteDeleteView, ClienteDetailView
from rest_framework import routers, serializers, viewsets

from app1.viewsets import ClienteViewSet
router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cliente', ClienteListView.as_view(),name="list_clientes"),
    path('cliente/create', ClienteCreateView.as_view(),name="cliente_create"),
    path('cliente/<pk>/update', ClienteUpdateView.as_view(),name="cliente_update"),
    path('cliente/<pk>', ClienteDetailView.as_view(),name="cliente_detail"),
    path('cliente/<pk>/delete', ClienteDeleteView.as_view(),name="cliente_delete"),
    path('direccion', DireccionView.as_view(), name='direccion_view'),
    path('template', EjemploTemplateView.as_view(), name='template'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
