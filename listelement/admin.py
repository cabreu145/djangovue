from django.contrib import admin

from .models import Estado_pieza, Categoria, Tipo_material, Pieza 

# Register your models here.

class Estado_piezaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo')

class Tipo_materialAdmin(admin.ModelAdmin):
    list_display = ('id','titulo')

class PiezaAdmin(admin.ModelAdmin):
    list_display = ('id','titulo')

admin.site.register(Estado_pieza, Estado_piezaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tipo_material, Tipo_materialAdmin)
admin.site.register(Pieza, PiezaAdmin)
