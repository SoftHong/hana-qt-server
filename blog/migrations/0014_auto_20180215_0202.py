# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-14 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_profile_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='day',
            field=models.CharField(choices=[(1, '월'), (2, '화'), (3, '수'), (4, '목'), (5, '금'), (6, '토'), (7, '일'), (8, '해당없음')], default=8, max_length=1),
        ),
    ]