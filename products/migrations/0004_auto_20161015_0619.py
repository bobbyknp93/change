# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-15 06:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20161013_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 11, 14, 6, 19, 56, 58086)),
        ),
    ]
