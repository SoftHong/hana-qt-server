# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 16:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20171230_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='external_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.ExternalAuthor'),
        ),
    ]
