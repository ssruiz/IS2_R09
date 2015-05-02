# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('US', '0002_us_proyecto_asociado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='us',
            name='proyecto_asociado',
            field=models.OneToOneField(null=True, blank=True, to='Proyecto.proyecto'),
            preserve_default=True,
        ),
    ]
