# Generated by Django 3.0.6 on 2020-05-29 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trans", "0081_announcement_notify"),
    ]

    operations = [
        migrations.AddField(
            model_name="component",
            name="push_branch",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Branch for pushing changes, leave empty to use repository branch",
                max_length=200,
                verbose_name="Push branch",
            ),
        ),
    ]
