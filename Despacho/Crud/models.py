from django.db import models
from django.utils import timezone


class Despacho(models.Model):
    nroSeguimiento = models.CharField(max_length=30, default='DEFAULT VALUE')
    nombreCliente = models.CharField(max_length=100, default='DEFAULT VALUE')
    direccionCliente = models.CharField(max_length=200, default='DEFAULT VALUE')
    horaLlegadaCrear = models.DateTimeField(auto_now_add=True)
    horaLlegadaActualizar = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'despacho' 

    def __str__(self):
        return self.nroSeguimiento
    
class Post_ventas(models.Model):
    nroSeguimiento = models.CharField(max_length=30, default='DEFAULT VALUE')
    nombreCliente = models.CharField(max_length=100, default='DEFAULT VALUE')
    direccionCliente = models.CharField(max_length=200, default='DEFAULT VALUE')
    horaLlegadaCrear = models.DateTimeField(auto_now_add=True)
    horaLlegadaActualizar = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post_venta' 

    def __str__(self):
        return self.nroSeguimiento


class Costo(models.Model):
    nroSeguimiento = models.CharField(max_length=30, default='DEFAULT VALUE')
    nombreCliente = models.CharField(max_length=100, default='DEFAULT VALUE')
    direccionCliente = models.CharField(max_length=200, default='DEFAULT VALUE')
    horaLlegadaCrear = models.DateTimeField(auto_now_add=True)
    horaLlegadaActualizar = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'costo' 

    def __str__(self):
        return self.nroSeguimiento