from django.db import models

# Create your models here.

class Categoria(models.Model):
    titulo = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Tipo_material(models.Model):
    titulo = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Estado_pieza(models.Model):
    titulo = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Pieza(models.Model):
    titulo = models.CharField(max_length=255)
    url_clean = models.CharField(max_length=255)
    descripcion = models.TextField()
    volumen = models.TextField()
    ancho = models.TextField()
    hora_estimada = models.TextField()
    hora_real = models.TextField()
    precio_costo = models.TextField()
    precio_venta = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado_pieza = models.ForeignKey(Estado_pieza, on_delete=models.CASCADE)
    tipo_material = models.ForeignKey(Tipo_material, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo