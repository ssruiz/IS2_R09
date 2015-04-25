# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Flujo', '0008_auto_20150425_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanban',
            name='fluj',
            field=models.ForeignKey(related_name='flujo', blank=True, to='Flujo.flujo', null=True),
            preserve_default=True,
        ),
    ]
