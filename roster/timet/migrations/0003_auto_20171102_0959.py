# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timet', '0002_lab_final_sec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab_final',
            name='sec',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]