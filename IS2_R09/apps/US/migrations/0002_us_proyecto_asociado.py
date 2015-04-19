# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0006_auto_20150416_0236'),
        ('US', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='us',
            name='proyecto_asociado',
            field=models.OneToOneField(null=True, to='Proyecto.proyecto'),
            preserve_default=True,
        ),
    ]
