from django.db import models

class Categoria (models.Model):
    nombre = models.CharField(max_length = 100)

    def __str__(self):
        return self.nombre

class Producto (models.Model):
    nombre = models.CharField(max_length = 100)
    precio = models.DecimalField(max_digits = 10,  decimal_places = 2)
    descripcion = models.TextField(max_length = 250, null = True)

    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null = True)
    
    def __str__(self):
        return self.nombre