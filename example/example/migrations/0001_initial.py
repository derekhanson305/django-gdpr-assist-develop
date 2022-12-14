# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-21 15:52
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import gdpr_assist


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HealthRecord",
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
                ("anonymised", models.BooleanField(default=False)),
                ("notes", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="MailingListLog",
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
                ("anonymised", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=254)),
                ("sent_at", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Person",
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
                ("anonymised", models.BooleanField(default=False)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
            ],
            options={"verbose_name_plural": "People"},
        ),
        migrations.CreateModel(
            name="PersonProfile",
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
                ("anonymised", models.BooleanField(default=False)),
                ("age", models.IntegerField(blank=True, null=True)),
                ("address", models.TextField(blank=True)),
                ("has_children", models.BooleanField(null=True)),
                (
                    "person",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=gdpr_assist.ANONYMISE(
                            django.db.models.deletion.SET_NULL
                        ),
                        to="example.Person",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="healthrecord",
            name="person",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="example.Person"
            ),
        ),
    ]
