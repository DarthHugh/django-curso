# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_da_alternativa', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_da_questao', models.CharField(max_length=200, verbose_name='Nome')),
                ('data_de_publicacao', models.DateTimeField(verbose_name='Data de Publicação')),
            ],
        ),
        migrations.AddField(
            model_name='alternativa',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquete.Questao'),
        ),
    ]
