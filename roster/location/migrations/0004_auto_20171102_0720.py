# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0003_auto_20171102_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='sec',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]
