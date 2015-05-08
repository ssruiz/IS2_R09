# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Flujo', '0010_auto_20150428_0624'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividad',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='actividad',
            name='order',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
