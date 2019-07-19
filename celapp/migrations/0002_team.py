# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-19 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name1', models.CharField(max_length=50)),
                ('grade1', models.IntegerField(default=0)),
                ('age1', models.IntegerField(default=0)),
                ('gender1', models.CharField(max_length=20)),
                ('expertise1', models.CharField(max_length=20)),
                ('student_name2', models.CharField(max_length=50)),
                ('grade2', models.IntegerField(default=0)),
                ('age2', models.IntegerField(default=0)),
                ('gender2', models.CharField(max_length=20)),
                ('expertise2', models.CharField(max_length=20)),
            ],
        ),
    ]
