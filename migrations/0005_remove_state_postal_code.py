# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 05:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eboard', '0004_auto_20170308_0445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='postal_code',
        ),
    ]
