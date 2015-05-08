# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Proyecto', '0007_auto_20150425_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='cliente',
            field=models.ForeignKey(related_name='cliente', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
