# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 06:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eboard', '0006_auto_20170308_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.BooleanField(default=False)),
                ('sms', models.BooleanField(default=False)),
                ('newsletter', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='bulletin',
            name='announcements',
            field=models.ManyToManyField(to='eboard.Announcement'),
        ),
        migrations.AddField(
            model_name='bulletin',
            name='events',
            field=models.ManyToManyField(to='eboard.Event'),
        ),
        migrations.AddField(
            model_name='bulletin',
            name='resources',
            field=models.ManyToManyField(to='eboard.Resource'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='announcer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eboard.Person'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eboard.Church'),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eboard.Church'),
        ),
        migrations.AlterField(
            model_name='church',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eboard.Location'),
        ),
        migrations.AlterField(
            model_name='event',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eboard.Church'),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='eboard.Location'),
        ),
        migrations.AlterField(
            model_name='person',
            name='church',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='member', to='eboard.Church'),
        ),
        migrations.AlterField(
            model_name='person',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='eboard.Location'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='church',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eboard.Church'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eboard.Person'),
        ),
        migrations.AddField(
            model_name='person',
            name='subscriptions',
            field=models.ManyToManyField(through='eboard.Subscription', to='eboard.Church'),
        ),
    ]
