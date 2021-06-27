from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import Pieza, Estado_pieza, Tipo_material, Categoria
from .serializer import PiezaSerializer, Estado_piezaSerializer, Tipo_materialSerializer, CategoriaSerializer


class PiezaViewSet(viewsets.ModelViewSet):
    queryset = Pieza.objects.all()
    serializer_class = PiezaSerializer

class Estado_piezaViewSet(viewsets.ModelViewSet):
    queryset = Estado_pieza.objects.all()
    serializer_class = Estado_piezaSerializer

class Tipo_materialViewSet (viewsets.ModelViewSet):
    queryset = Tipo_material.objects.all()
    serializer_class = Tipo_materialSerializer

    @action(detail=True, methods=['get'])
    def piezas(self, request, pk=None):
        queryset = Pieza.objects.filter(tipo_material_id=pk)
        serializer = PiezaSerializer(queryset, many=True)
        return Response(serializer.data) 

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @action(detail=True, methods=['get'])
    def piezas(self, request, pk=None):
        queryset = Pieza.objects.filter(categoria_id=pk)
        serializer = PiezaSerializer(queryset, many=True)
        return Response(serializer.data) 