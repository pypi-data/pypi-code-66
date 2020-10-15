# Generated by Django 2.0.13 on 2019-05-22 15:17

import django.contrib.postgres.fields.jsonb
import django.core.validators
import django.db.models.deletion
import django_geosource.mixins
import django_geosource.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("contenttypes", "0002_remove_content_type_name")]

    operations = [
        migrations.CreateModel(
            name="Field",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("label", models.CharField(max_length=255)),
                (
                    "data_type",
                    models.CharField(
                        choices=[
                            (1, django_geosource.models.FieldTypes(1)),
                            (2, django_geosource.models.FieldTypes(2)),
                            (3, django_geosource.models.FieldTypes(3)),
                            (4, django_geosource.models.FieldTypes(4)),
                            (5, django_geosource.models.FieldTypes(5)),
                        ],
                        max_length=255,
                    ),
                ),
                ("sample", django.contrib.postgres.fields.jsonb.JSONField(default=[])),
            ],
        ),
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField(blank=True)),
                ("id_field", models.CharField(default="id", max_length=255)),
                (
                    "geom_type",
                    models.IntegerField(
                        choices=[
                            (0, django_geosource.models.GeometryTypes(0)),
                            (1, django_geosource.models.GeometryTypes(1)),
                            (3, django_geosource.models.GeometryTypes(3)),
                            (4, django_geosource.models.GeometryTypes(4)),
                            (5, django_geosource.models.GeometryTypes(5)),
                            (6, django_geosource.models.GeometryTypes(6)),
                            (7, django_geosource.models.GeometryTypes(7)),
                        ]
                    ),
                ),
                ("status", models.NullBooleanField(default=None)),
            ],
            options={"abstract": False, "base_manager_name": "objects"},
            bases=(models.Model, django_geosource.mixins.CeleryCallMethodsMixin),
        ),
        migrations.CreateModel(
            name="GeoJSONSource",
            fields=[
                (
                    "source_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_geosource.Source",
                    ),
                ),
                ("file", models.FileField(upload_to="geosource/")),
            ],
            options={"abstract": False, "base_manager_name": "objects"},
            bases=("django_geosource.source",),
        ),
        migrations.CreateModel(
            name="PostGISSource",
            fields=[
                (
                    "source_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="django_geosource.Source",
                    ),
                ),
                (
                    "db_host",
                    models.CharField(
                        max_length=255,
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="(?:(?:25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)(?:\\.(?:25[0-5]|2[0-4]\\d|[0-1]?\\d?\\d)){3}|\\[[0-9a-f:\\.]+\\]|([a-z¡-\uffff0-9](?:[a-z¡-\uffff0-9-]{0,61}[a-z¡-\uffff0-9])?(?:\\.(?!-)[a-z¡-\uffff0-9-]{1,63}(?<!-))*\\.(?!-)(?:[a-z¡-\uffff-]{2,63}|xn--[a-z0-9]{1,59})(?<!-)\\.?|localhost))"
                            )
                        ],
                    ),
                ),
                ("db_port", models.IntegerField(default=5432)),
                ("db_username", models.CharField(max_length=63)),
                ("db_password", models.CharField(max_length=255)),
                ("db_name", models.CharField(max_length=63)),
                ("query", models.TextField()),
                ("geom_field", models.CharField(max_length=255)),
                ("refresh", models.IntegerField()),
            ],
            options={"abstract": False, "base_manager_name": "objects"},
            bases=("django_geosource.source",),
        ),
        migrations.AddField(
            model_name="source",
            name="polymorphic_ctype",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="polymorphic_django_geosource.source_set+",
                to="contenttypes.ContentType",
            ),
        ),
        migrations.AddField(
            model_name="field",
            name="source",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="fields",
                to="django_geosource.Source",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="field", unique_together={("source", "name")}
        ),
    ]
