# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0006_auto_20150416_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='sprint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=100)),
                ('fecha_inicio', models.DateField(null=True, blank=True)),
                ('fecha_fin', models.DateField(null=True, blank=True)),
                ('proyect', models.ForeignKey(blank=True, to='Proyecto.proyecto', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
