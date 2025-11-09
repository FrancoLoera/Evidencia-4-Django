from django.db import models

# Create your models here.
class Relacion(models.Model):
    descripcion = models.CharField(max_length = 50, unique = True)
    
    def __str__(self):
        return self.descripcion
    
    def save(self, *args, **kwargs):
        if self.descripcion:
            self.descripcion = self.descripcion.upper()
            
        super().save(*args, **kwargs)

class Contacto(models.Model):
    nombre = models.CharField(max_length = 50)
    primerApellido = models.CharField(max_length = 50)
    segundoApellido = models.CharField(max_length = 50, blank = True, null = False)
    alias = models.CharField(max_length = 50, blank = True, null = False)
    relacion = models.ForeignKey(Relacion, on_delete = models.PROTECT)
    telefono = models.CharField(max_length=10, unique = True)
    correo = models.EmailField(max_length=254, unique = True, blank = True, null = False)
    
    def save(self, *args, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()
            
        if self.primerApellido:
            self.primerApellido = self.primerApellido.upper()
            
        if self.segundoApellido:
            self.segundoApellido = self.segundoApellido.upper()
            
        if self.alias:
            self.alias = self.alias.upper()
            
        if self.telefono:
            self.telefono = self.telefono.upper()
            
        if self.correo:
            self.correo = self.correo.upper()

        super().save(*args, **kwargs)
        
    def __str__(self):
        base = f"{self.nombre} {self.primerApellido}"

        if self.segundoApellido:
            base += f" {self.segundoApellido}"
        
        base += f" - {self.telefono}"
        
        if self.correo:
            base += f" - {self.correo}"

        return base