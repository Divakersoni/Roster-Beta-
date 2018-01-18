# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-08 05:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timet', '0006_master_final_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master_final',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0),
        ),
    ]
