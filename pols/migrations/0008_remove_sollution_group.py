# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pols', '0007_auto_20150525_1820'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sollution',
            name='group',
        ),
    ]
