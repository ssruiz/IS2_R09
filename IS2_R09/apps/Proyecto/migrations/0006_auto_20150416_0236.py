# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Flujo', '0002_remove_actividad_estado'),
        ('Proyecto', '0005_proyecto_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='flujos',
            field=models.ManyToManyField(to='Flujo.flujo', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='estado',
            field=models.CharField(default=b'Iniciado', max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
