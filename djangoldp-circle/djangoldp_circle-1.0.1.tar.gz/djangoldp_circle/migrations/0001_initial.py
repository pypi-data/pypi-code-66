# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-10-15 15:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangoldp.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlid', djangoldp.fields.LDPUrlField(blank=True, null=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('creationDate', models.DateField(auto_now_add=True)),
                ('jabberID', models.CharField(blank=True, max_length=255, null=True)),
                ('jabberRoom', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owned_circles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CircleMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlid', djangoldp.fields.LDPUrlField(blank=True, null=True, unique=True)),
                ('circle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='djangoldp_circle.Circle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='circle',
            name='team',
            field=models.ManyToManyField(blank=True, through='djangoldp_circle.CircleMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
