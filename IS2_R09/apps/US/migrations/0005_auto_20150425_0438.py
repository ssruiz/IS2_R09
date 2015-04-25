# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('US', '0004_auto_20150419_2320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='us',
            name='flujo_asignado',
        ),
        migrations.RemoveField(
            model_name='us',
            name='proyecto_asociado',
        ),
    ]
