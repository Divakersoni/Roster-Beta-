# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 09:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0006_auto_20171102_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='sec',
        ),
    ]
