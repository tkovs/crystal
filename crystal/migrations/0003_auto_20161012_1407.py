# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0002_prova_dificuldade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prova',
            name='titulo',
            field=models.CharField(max_length=40),
        ),
    ]
