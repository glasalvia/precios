# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_precios', '0002_auto_20180928_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='cantidad',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]