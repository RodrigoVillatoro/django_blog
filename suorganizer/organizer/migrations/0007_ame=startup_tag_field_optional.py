# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0006_newslink_unique_together_slug_startup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(blank=True, to='organizer.Tag'),
        ),
    ]