# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Flujo', '0003_auto_20150417_1836'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='us',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=200)),
                ('tiempo_estimado', models.IntegerField(null=True, blank=True)),
                ('tiempo_trabajado', models.IntegerField(null=True, blank=True)),
                ('prioridad', models.CharField(max_length=1, choices=[(b'A', b'Alta'), (b'M', b'Media'), (b'B', b'Baja')])),
                ('flujo_asignado', models.OneToOneField(null=True, blank=True, to='Flujo.flujo')),
                ('usuario_asignado', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
