# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pols', '0008_remove_sollution_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='sollution',
            name='group',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
