# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-09-24 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0060_supplier_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderline',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now, verbose_name='created on'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderline',
            name='modified_on',
            field=models.DateTimeField(auto_now=True, db_index=True, default=django.utils.timezone.now, verbose_name='modified on'),
        ),
    ]
