# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('US', '0003_auto_20150419_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='us',
            name='flujo_asignado',
            field=models.ForeignKey(blank=True, to='Flujo.flujo', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='us',
            name='proyecto_asociado',
            field=models.ForeignKey(blank=True, to='Proyecto.proyecto', null=True),
            preserve_default=True,
        ),
    ]
