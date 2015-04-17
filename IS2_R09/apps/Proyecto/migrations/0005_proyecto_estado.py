# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0004_auto_20150410_2207'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='estado',
            field=models.CharField(default=b'iniciado', max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
