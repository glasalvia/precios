# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-28 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_precios', '0005_auto_20180928_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen_url',
            field=models.FileField(upload_to='documents/'),
        ),
    ]