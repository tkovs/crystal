# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160606161117 on 2016-10-11 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crystal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prova',
            name='dificuldade',
            field=models.IntegerField(choices=[(1, 'FÁCIL'), (2, 'INICIANTE'), (3, 'COMUM'), (4, 'DIFÍCIL'), (5, 'MESTRE')], default=3),
        ),
    ]