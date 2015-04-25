# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Flujo', '0004_auto_20150425_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='flujo',
            name='actividades',
            field=models.ManyToManyField(to='Flujo.actividad'),
            preserve_default=True,
        ),
    ]
