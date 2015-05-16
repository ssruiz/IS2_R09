# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('US', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='flujo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=30)),
                ('actividades', models.ManyToManyField(to='Flujo.actividad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='kanban',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default=b'td', max_length=2, null=True, blank=True, choices=[(b'td', b'to do'), (b'dg', b'doing'), (b'de', b'done')])),
                ('prioridad', models.CharField(max_length=1, null=True, blank=True)),
                ('actividad', models.ForeignKey(related_name='actividad', blank=True, to='Flujo.actividad', null=True)),
                ('fluj', models.ForeignKey(related_name='flujo', blank=True, to='Flujo.flujo', null=True)),
                ('us', models.ForeignKey(related_name='user_story', blank=True, to='US.us', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='flujo',
            name='user_stories',
            field=models.ManyToManyField(related_name='userstories', null=True, through='Flujo.kanban', to='US.us', blank=True),
            preserve_default=True,
        ),
    ]
