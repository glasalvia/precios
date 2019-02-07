# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import pandas as pd


db  = sqlite3.connect('D:\\python27\\Proyectos\\db.sqlite3')
cursor = db.cursor()
cursor.execute('''select* from api_precios_cadena''')

print(cursor.fetchall())

db.close()

def api_precios(request):
    if request.method == 'GET':
        return HttpResponse(consulta_1)








