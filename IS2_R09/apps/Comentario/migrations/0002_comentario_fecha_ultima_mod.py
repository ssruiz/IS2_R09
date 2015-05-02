# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Comentario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='fecha_ultima_mod',
            field=models.DateField(default=datetime.datetime(2015, 5, 2, 5, 40, 54, 982576, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
