# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-17 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FECHA_CREACION', models.CharField(max_length=10)),
                ('NOMBRES', models.CharField(max_length=20)),
                ('APPELLIDOS', models.CharField(max_length=20)),
                ('DATOS_ADICIONALES', models.CharField(max_length=20)),
                ('DNI', models.CharField(max_length=20)),
                ('HORA_CREACION', models.CharField(max_length=20)),
                ('FECHA_DE_NACIMIENTO', models.CharField(max_length=10)),
                ('NACIONALIDAD', models.CharField(max_length=20)),
            ],
        ),
    ]