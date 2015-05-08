# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('US', '0009_auto_20150502_0449'),
        ('Sprint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='ust',
            field=models.ManyToManyField(to='US.us', null=True, blank=True),
            preserve_default=True,
        ),
    ]
