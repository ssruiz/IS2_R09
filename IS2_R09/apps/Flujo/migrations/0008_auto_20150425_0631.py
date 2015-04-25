# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Flujo', '0007_auto_20150425_0520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kanban',
            name='actividad',
            field=models.ForeignKey(related_name='actividad', blank=True, to='Flujo.actividad', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='kanban',
            name='estado',
            field=models.CharField(default=b'td', max_length=2, null=True, blank=True, choices=[(b'td', b'to do'), (b'dg', b'doing'), (b'de', b'done')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='kanban',
            name='us',
            field=models.ForeignKey(related_name='user_story', blank=True, to='US.us', null=True),
            preserve_default=True,
        ),
    ]
