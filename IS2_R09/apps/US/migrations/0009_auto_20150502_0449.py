# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adjunto', '__first__'),
        ('Comentario', '0001_initial'),
        ('US', '0008_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='us',
            name='adjuntos',
            field=models.ManyToManyField(to='Adjunto.adjunto', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='us',
            name='comentarios',
            field=models.ManyToManyField(to='Comentario.comentario', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='us',
            name='proyecto_asociado',
            field=models.ForeignKey(blank=True, to='Proyecto.proyecto', null=True),
            preserve_default=True,
        ),
    ]
