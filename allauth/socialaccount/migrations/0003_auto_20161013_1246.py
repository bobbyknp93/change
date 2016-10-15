# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-13 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0002_auto_20161013_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='provider',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter'), ('linkedin_oauth2', 'LinkedIn'), ('google', 'Google')], max_length=30, verbose_name='provider'),
        ),
        migrations.AlterField(
            model_name='socialapp',
            name='provider',
            field=models.CharField(choices=[('facebook', 'Facebook'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter'), ('linkedin_oauth2', 'LinkedIn'), ('google', 'Google')], max_length=30, verbose_name='provider'),
        ),
    ]
