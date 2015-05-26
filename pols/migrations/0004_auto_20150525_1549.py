# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pols', '0003_auto_20150524_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sollution',
            name='submitter',
            field=models.TextField(max_length=30),
        ),
    ]
