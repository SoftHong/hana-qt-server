# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-23 05:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171223_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='book',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='external_author',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='profile_link',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='publisher',
            field=models.CharField(blank=True, default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
