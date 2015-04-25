# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Flujo', '0005_flujo_actividades'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kanban',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='kanban',
            name='fluj',
        ),
        migrations.RemoveField(
            model_name='kanban',
            name='us',
        ),
        migrations.RemoveField(
            model_name='flujo',
            name='user_stories',
        ),
        migrations.DeleteModel(
            name='kanban',
        ),
    ]
