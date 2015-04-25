# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0007_auto_20150425_0404'),
        ('US', '0005_auto_20150425_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='us',
            name='proyecto_asociado',
            field=models.ForeignKey(blank=True, to='Proyecto.proyecto', null=True),
            preserve_default=True,
        ),
    ]
