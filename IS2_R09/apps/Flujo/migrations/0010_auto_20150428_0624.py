# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Flujo', '0009_auto_20150425_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='nombre',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
