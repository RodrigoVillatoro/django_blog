# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 06:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


FLATPAGES = [
    {
        'title': 'About',
        'url': '/about/',
        'content': ''
    }
]


def add_flatpages_data(apps, schema_editor):
    FlatPage = apps.get_model('flatpages', 'FlatPage')
    Site = apps.get_model('sites', 'Site')
    site_id = getattr(settings, 'SITE_ID', 1)
    current_site = Site.objects.get(pk=site_id)
    for page_dict in FLATPAGES:
        new_page = FlatPage.objects.create(
            title=page_dict['title'],
            url=page_dict['url'],
            content=page_dict['content']
        )
        new_page.sites.add(current_site)


def remove_flatpages_data(apps, schema_editor):
    FlatPage = apps.get_model('flatpages', 'FlatPage')
    for page_dict in FLATPAGES:
        page = FlatPage.objects.get(
            url=page_dict['url']
        )
        page.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_sites_data'),
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_flatpages_data, remove_flatpages_data)
    ]
