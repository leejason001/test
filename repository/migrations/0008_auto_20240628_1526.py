# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-06-28 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0007_auto_20240625_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='troubles',
            name='mark',
            field=models.IntegerField(blank=True, choices=[(1, 'bad'), (2, 'common'), (3, 'good')], null=True),
        ),
    ]
