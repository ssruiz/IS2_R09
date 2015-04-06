# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Proyecto', '0002_auto_20150404_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('miembro', models.ForeignKey(related_name='usuario_proyec', to=settings.AUTH_USER_MODEL)),
                ('proyect', models.ForeignKey(related_name='proyecto', to='Proyecto.proyecto')),
                ('rol', models.ForeignKey(related_name='rol', to='auth.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='proyecto',
            name='equipo',
        ),
        migrations.AddField(
            model_name='proyecto',
            name='miembro',
            field=models.ManyToManyField(related_name='equipo', null=True, through='Proyecto.Equipo', to=settings.AUTH_USER_MODEL, blank=True),
            preserve_default=True,
        ),
    ]
