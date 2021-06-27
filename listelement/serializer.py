from rest_framework import serializers

from .models import Pieza,Tipo_material,Categoria ,Estado_pieza

class PiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pieza
        fields = '__all__'
        

class Tipo_materialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_material
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class Estado_piezaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_pieza
        fields = '__all__'
