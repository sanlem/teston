# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=100)),
                ('questions_number', models.IntegerField()),
                ('password', models.CharField(unique=True, max_length=6)),
                ('owner', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('variant_1', models.CharField(max_length=100)),
                ('variant_2', models.CharField(max_length=100)),
                ('variant_3', models.CharField(max_length=100)),
                ('variant_4', models.CharField(max_length=100)),
                ('poll', models.ForeignKey(to='pols.Poll')),
            ],
        ),
        migrations.CreateModel(
            name='Sollution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitter', models.CharField(max_length=30)),
                ('group', models.CharField(max_length=30)),
                ('point', models.IntegerField()),
                ('poll', models.ForeignKey(to='pols.Poll')),
            ],
        ),
    ]
