# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-09 17:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file
import filer.fields.folder


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('shuup', '0043_order_customer_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.CASCADE, related_name='media_file', to='filer.File', verbose_name='file')),
                ('shops', models.ManyToManyField(help_text='Select which shops you would like the files to be visible in.', related_name='media_files', to='shuup.Shop', verbose_name='shops')),
            ],
        ),
        migrations.CreateModel(
            name='MediaFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', filer.fields.folder.FilerFolderField(on_delete=django.db.models.deletion.CASCADE, related_name='media_folder', to='filer.Folder', verbose_name='folder')),
                ('shops', models.ManyToManyField(help_text='Select which shops you would like the folder to be visible in.', related_name='media_folders', to='shuup.Shop', verbose_name='shops')),
            ],
        ),
    ]
