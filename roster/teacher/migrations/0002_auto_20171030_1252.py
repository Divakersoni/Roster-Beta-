# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='teaching_hours_a_day',
        ),
        migrations.AddField(
            model_name='teacher',
            name='teaching_hours_a_day_subject1',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teaching_hours_a_day_subject2',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teaching_hours_a_day_subject3',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='teaching_hours_a_day_subject4',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
