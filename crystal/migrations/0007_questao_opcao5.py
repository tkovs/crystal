# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0006_auto_20161023_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='questao',
            name='opcao5',
            field=models.CharField(default='Nenhuma das alternativas', max_length=150),
        ),
    ]
