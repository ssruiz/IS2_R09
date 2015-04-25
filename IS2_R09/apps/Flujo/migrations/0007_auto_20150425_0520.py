# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('US', '0006_us_proyecto_asociado'),
        ('Flujo', '0006_auto_20150425_0449'),
    ]

    operations = [
        migrations.CreateModel(
            name='kanban',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(default=b'td', max_length=2, choices=[(b'td', b'to do'), (b'dg', b'doing'), (b'de', b'done')])),
                ('actividad', models.ForeignKey(related_name='actividad', to='Flujo.actividad')),
                ('fluj', models.ForeignKey(related_name='flujo', to='Flujo.flujo')),
                ('us', models.ForeignKey(related_name='user_story', to='US.us')),
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
