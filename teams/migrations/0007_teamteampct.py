# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-15 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_auto_20180407_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamTeamPct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=10)),
                ('gp', models.IntegerField()),
                ('ast_prtg', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('stl_prtg', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('blk_prtg', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('tov_prtg', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('fls_prtg', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]