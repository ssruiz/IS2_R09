# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0006_auto_20150416_0236'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='duracion_sprint',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='sprint_actual',
            field=models.CharField(max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
