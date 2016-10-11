# -*- coding: utf-8 -*-
# Generated by Django 1.11.dev20160606161117 on 2016-10-11 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prova',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=100)),
                ('resposta', models.IntegerField()),
                ('opcao1', models.CharField(max_length=60)),
                ('opcao2', models.CharField(max_length=60)),
                ('opcao3', models.CharField(max_length=60)),
                ('opcao4', models.CharField(max_length=60)),
                ('prova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crystal.Prova')),
            ],
        ),
        migrations.CreateModel(
            name='Realizado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prova', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crystal.Prova')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('pontuacao', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='realizado',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crystal.Usuario'),
        ),
        migrations.AddField(
            model_name='prova',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crystal.Usuario'),
        ),
    ]