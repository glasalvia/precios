# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from models import Cadena, Producto, Precio
import sqlite3
import pandas as pd
from django.core import serializers

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

consulta_1 = serializers.serialize('json', Producto.objects.all(), fields=('producto','marca'))
print(consulta_1)

def api_precios(request):
    if request.method == 'GET':
        return HttpResponse(consulta_1)

