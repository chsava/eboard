# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 06:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eboard', '0005_remove_state_postal_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=4096)),
                ('date_posted', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Bulletin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('notes', models.TextField(max_length=4096, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='church',
            name='conference_id',
        ),
        migrations.RemoveField(
            model_name='church',
            name='contact1_id',
        ),
        migrations.RemoveField(
            model_name='church',
            name='contact2_id',
        ),
        migrations.RemoveField(
            model_name='church',
            name='contact3_id',
        ),
        migrations.RemoveField(
            model_name='church',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='church',
            name='division_id',
        ),
        migrations.RemoveField(
            model_name='church',
            name='location_id',
        ),
        migrations.RemoveField(
            model_name='church',
            name='state_code',
        ),
        migrations.RemoveField(
            model_name='church',
            name='union_id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='church_id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='contact_id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='location_id',
        ),
        migrations.RemoveField(
            model_name='event',
            name='organizer_id',
        ),
        migrations.RemoveField(
            model_name='location',
            name='church_id',
        ),
        migrations.RemoveField(
            model_name='location',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='location',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='location',
            name='person_id',
        ),
        migrations.RemoveField(
            model_name='location',
            name='state_code',
        ),
        migrations.RemoveField(
            model_name='person',
            name='church_id',
        ),
        migrations.RemoveField(
            model_name='person',
            name='country_code',
        ),
        migrations.RemoveField(
            model_name='person',
            name='location_id',
        ),
        migrations.RemoveField(
            model_name='person',
            name='state_code',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='author_id',
        ),
        migrations.RemoveField(
            model_name='resource',
            name='church_id',
        ),
        migrations.RemoveField(
            model_name='state',
            name='country_code',
        ),
        migrations.AddField(
            model_name='church',
            name='conference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='eboard.Church'),
        ),
        migrations.AddField(
            model_name='church',
            name='contact1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='eboard.Person'),
        ),
        migrations.AddField(
            model_name='church',
            name='contact2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='eboard.Person'),
        ),
        migrations.AddField(
            model_name='church',
            name='contact3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='eboard.Person'),
        ),
        migrations.AddField(
            model_name='church',
            name='country',
            field=models.ForeignKey(default=b'usa', on_delete=django.db.models.deletion.PROTECT, to='eboard.Country'),
        ),
        migrations.AddField(
            model_name='church',
            name='division',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='eboard.Church'),
        ),
        migrations.AddField(
            model_name='church',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eboard.Location'),
        ),
        migrations.AddField(
            model_name='church',
            name='state',
            field=models.ForeignKey(default=b'ca', on_delete=django.db.models.deletion.PROTECT, to='eboard.State'),
        ),
        migrations.AddField(
            model_name='church',
            name='union',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='eboard.Church'),
        ),
        migrations.AddField(
            model_name='event',
            name='church',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eboard.Church'),
        ),
        migrations.AddField(
            model_name='event',
            name='contact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='eboard.Person'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eboard.Location'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='eboard.Person'),
        ),
        migrations.AddField(
            model_name='location',
            name='country',
            field=models.ForeignKey(default=b'usa', on_delete=django.db.models.deletion.PROTECT, to='eboard.Country'),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=models.ForeignKey(default=b'ca', on_delete=django.db.models.deletion.PROTECT, to='eboard.State'),
        ),
        migrations.AddField(
            model_name='person',
            name='church',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eboard.Church'),
        ),
        migrations.AddField(
            model_name='person',
            name='country',
            field=models.ForeignKey(default=b'usa', on_delete=django.db.models.deletion.PROTECT, to='eboard.Country'),
        ),
        migrations.AddField(
            model_name='person',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eboard.Location'),
        ),
        migrations.AddField(
            model_name='person',
            name='state',
            field=models.ForeignKey(default=b'ca', on_delete=django.db.models.deletion.PROTECT, to='eboard.State'),
        ),
        migrations.AddField(
            model_name='resource',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eboard.Person'),
        ),
        migrations.AddField(
            model_name='resource',
            name='church',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eboard.Church'),
        ),
        migrations.AddField(
            model_name='state',
            name='country',
            field=models.ForeignKey(default=b'usa', on_delete=django.db.models.deletion.PROTECT, to='eboard.Country'),
        ),
        migrations.AlterField(
            model_name='church',
            name='language1',
            field=models.ForeignKey(default=b'eng', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='eboard.Language'),
        ),
        migrations.AlterField(
            model_name='church',
            name='language2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='eboard.Language'),
        ),
        migrations.AlterField(
            model_name='country',
            name='language1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='eboard.Language'),
        ),
        migrations.AlterField(
            model_name='country',
            name='language2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='eboard.Language'),
        ),
        migrations.AlterField(
            model_name='event',
            name='language1',
            field=models.ForeignKey(default=b'eng', on_delete=django.db.models.deletion.PROTECT, related_name='+', to='eboard.Language'),
        ),
        migrations.AlterField(
            model_name='event',
            name='language2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='eboard.Language'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='language',
            field=models.ForeignKey(default=b'eng', on_delete=django.db.models.deletion.PROTECT, to='eboard.Language'),
        ),
        migrations.AlterField(
            model_name='state',
            name='language',
            field=models.ForeignKey(default=b'eng', on_delete=django.db.models.deletion.PROTECT, to='eboard.Language'),
        ),
        migrations.AddField(
            model_name='bulletin',
            name='church',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eboard.Church'),
        ),
        migrations.AddField(
            model_name='bulletin',
            name='language',
            field=models.ForeignKey(default=b'eng', on_delete=django.db.models.deletion.PROTECT, to='eboard.Language'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='announcer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eboard.Person'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='church',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eboard.Church'),
        ),
        migrations.AddField(
            model_name='announcement',
            name='language',
            field=models.ForeignKey(default=b'eng', on_delete=django.db.models.deletion.PROTECT, to='eboard.Language'),
        ),
    ]
