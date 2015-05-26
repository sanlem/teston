# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pols', '0005_question_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['number']},
        ),
    ]
