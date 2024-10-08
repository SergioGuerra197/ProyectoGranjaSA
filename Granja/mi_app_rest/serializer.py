from rest_framework import serializers
from .models import *


class clienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        # fields = ('fullname', 'nickname')
        fields = '__all__'

class porcinoSerializer(serializers.ModelSerializer):
    
    razas_idrazas = serializers.PrimaryKeyRelatedField(queryset=Razas.objects.all())
    clientes_cedula = serializers.PrimaryKeyRelatedField(queryset=Clientes.objects.all())

    class Meta:
        model = Porcinos
        fields = '__all__'

class alimentosSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Alimentacion
        fields = '__all__'

class porcinosHasAlimentacionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = PorcinosHasAlimentacion
        fields = '__all__'
        

class razasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Razas
        fields = '__all__'