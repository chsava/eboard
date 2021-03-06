# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eboard', '0002_church_country_language_location_person_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=4096)),
                ('location_id', models.PositiveIntegerField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('contact_id', models.PositiveIntegerField()),
                ('organizer_id', models.PositiveIntegerField(null=True)),
                ('church_id', models.PositiveIntegerField()),
                ('event_type', models.CharField(choices=[('WO', 'Worship'), ('SS', 'Sabbath School'), ('SE', 'Sermon'), ('PO', 'Potluck'), ('RE', 'Retreat'), ('CO', 'Conference')], max_length=2)),
                ('language1', models.CharField(default='eng', max_length=3)),
                ('language2', models.CharField(max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author_id', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=4096)),
                ('url', models.CharField(max_length=255)),
                ('date_posted', models.DateField()),
                ('church_id', models.PositiveIntegerField()),
                ('language', models.CharField(default='eng', max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='church',
            name='language1',
            field=models.CharField(default='eng', max_length=3),
        ),
        migrations.AlterField(
            model_name='state',
            name='language',
            field=models.CharField(default='eng', max_length=3),
        ),
    ]
