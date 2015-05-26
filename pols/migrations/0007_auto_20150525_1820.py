# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pols', '0006_auto_20150525_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sollution',
            old_name='point',
            new_name='mark',
        ),
    ]
