from rest_framework import viewsets

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

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer 