# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_resolver', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='redirects',
            name='url_status',
            field=models.IntegerField(choices=[(301, 301), (302, 302)], default=301),
        ),
    ]
