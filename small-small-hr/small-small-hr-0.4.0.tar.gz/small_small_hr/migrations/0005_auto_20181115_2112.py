# Generated by Django 2.1.2 on 2018-11-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('small_small_hr', '0004_auto_20180725_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffdocument',
            name='public',
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text='If public, it will be available to everyone.',
                verbose_name='Public'),
        ),
        migrations.AlterField(
            model_name='staffprofile',
            name='overtime_allowed',
            field=models.BooleanField(
                blank=True, default=False, verbose_name='Overtime allowed'),
        ),
    ]
