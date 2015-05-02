# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('US', '0006_us_proyecto_asociado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='us',
            name='prioridad',
            field=models.CharField(max_length=1, choices=[(b'1', b'Alta'), (b'2', b'Media'), (b'3', b'Baja')]),
            preserve_default=True,
        ),
    ]
