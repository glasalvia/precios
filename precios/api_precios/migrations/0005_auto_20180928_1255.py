# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 15:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_precios', '0004_auto_20180928_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadena',
            name='id_cadena',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='precio',
            name='id_precio',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
