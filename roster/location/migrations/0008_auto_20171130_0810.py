# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-30 08:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0007_remove_lab_sec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='sec1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sec1', to='semclass.Sec'),
        ),
    ]
