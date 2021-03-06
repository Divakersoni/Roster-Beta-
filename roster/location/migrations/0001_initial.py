# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-29 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.SmallIntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')], default=0)),
                ('room_no', models.CharField(max_length=10)),
                ('sec', models.CharField(default='A', max_length=10)),
                ('alt_name', models.CharField(default='LH1', max_length=10, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('added_on', models.DateTimeField(null=True, verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block', models.SmallIntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')], default=0)),
                ('lab_no', models.CharField(max_length=10)),
                ('alt_name', models.CharField(default='cp1', max_length=10, null=True)),
                ('status', models.SmallIntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=0)),
                ('added_on', models.DateTimeField(null=True, verbose_name='date added')),
            ],
        ),
    ]
