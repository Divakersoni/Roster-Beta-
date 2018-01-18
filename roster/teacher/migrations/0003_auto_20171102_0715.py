# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-02 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20171030_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='added_on',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='added_on',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='added_on',
        ),
        migrations.AddField(
            model_name='teacher',
            name='total_teaching_hours_a_day',
            field=models.SmallIntegerField(default=4),
        ),
    ]
