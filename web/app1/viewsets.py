from rest_framework import  viewsets
from app1.models import Cliente
from app1.serializer import ClienteSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer