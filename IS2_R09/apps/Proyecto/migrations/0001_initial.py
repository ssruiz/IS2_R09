# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField(max_length=200)),
                ('fecha_creacion', models.DateField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('cliente', models.OneToOneField(related_name='cliente', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('equipo', models.ManyToManyField(related_name='equipo', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
