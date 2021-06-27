from django.conf.urls import url
from django.urls import path

from rest_framework import routers

from .viewsets import PiezaViewSet, Estado_piezaViewSet, Tipo_materialViewSet, CategoriaViewSet

route = routers.SimpleRouter()
route.register('pieza',PiezaViewSet)
route.register('estado_pieza',Estado_piezaViewSet)
route.register('tipo_material',Tipo_materialViewSet)
route.register('categoria',CategoriaViewSet)

urlpatterns = route.urls