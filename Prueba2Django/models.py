from django.db import models

class Seminario(models.Model):
    nombre = models.CharField(max_length=50)
    telcontacto = models.IntegerField()
    fechaseminario = models.DateField()
    empresa = models.CharField(max_length=50)
    email = models.EmailField()  
    profesion = models.CharField(max_length=50)
    observacion = models.CharField(max_length=250, blank=True)

    
