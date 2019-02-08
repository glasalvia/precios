# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django_pandas.managers import DataFrameManager


Lista_Unidades = (
    ('LT','LT'),
    ('GR', 'GR'),
    ('KL','KL'),
)


class Cadena(models.Model):
    id_cadena = models.AutoField(primary_key=True)
    cadena = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)

    def __unicode__(self):
       return self.cadena

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=255, blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    unidad = models.CharField(max_length=2, choices=Lista_Unidades, default='lt')
    cantidad = models.DecimalField(max_digits=5, decimal_places=2) 
    imagen = models.ImageField(upload_to='documents/', blank=True, null=True)

    def __unicode__(self):
       return self.producto+' '+self.marca 


class Precio(models.Model):
    id_precio = models.AutoField(primary_key=True)
    fecha_hora = models.DateTimeField(auto_now_add=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_cadena = models.ForeignKey(Cadena, on_delete=models.CASCADE)
    precio_c_descuento = models.DecimalField(max_digits=5, decimal_places=2) 
    precio = models.DecimalField(max_digits=5, decimal_places=2) 
    url = models.URLField(db_column='URL', max_length=255, blank=True, null=True)
    pdobjects = DataFrameManager() 

