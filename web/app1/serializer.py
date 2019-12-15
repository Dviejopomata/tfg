from rest_framework import  serializers
from app1.models import Cliente
class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'identificacion', 'nombre']
