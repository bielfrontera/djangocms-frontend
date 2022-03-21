# Generated by Django 3.2.12 on 2022-03-21 08:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import djangocms_frontend.contrib.forms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("djangocms_frontend", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CharField",
            fields=[],
            options={
                "verbose_name": "Character field",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=(
                djangocms_frontend.contrib.forms.models.FormFieldMixin,
                "djangocms_frontend.frontenduiitem",
            ),
        ),
        migrations.CreateModel(
            name="Form",
            fields=[],
            options={
                "verbose_name": "Form",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
        migrations.CreateModel(
            name="BooleanField",
            fields=[],
            options={
                "verbose_name": "Boolean field",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=(
                djangocms_frontend.contrib.forms.models.FormFieldMixin,
                "djangocms_frontend.frontenduiitem",
            ),
        ),
        migrations.CreateModel(
            name="Select",
            fields=[],
            options={
                "verbose_name": "Select",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=(
                djangocms_frontend.contrib.forms.models.FormFieldMixin,
                "djangocms_frontend.frontenduiitem",
            ),
        ),
        migrations.CreateModel(
            name="SubmitButton",
            fields=[],
            options={
                "verbose_name": "Submit button",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=(
                djangocms_frontend.contrib.forms.models.FormFieldMixin,
                "djangocms_frontend.frontenduiitem",
            ),
        ),
        migrations.CreateModel(
            name="TextareaField",
            fields=[],
            options={
                "verbose_name": "Text field",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=(
                djangocms_frontend.contrib.forms.models.FormFieldMixin,
                "djangocms_frontend.frontenduiitem",
            ),
        ),
        migrations.CreateModel(
            name="FormEntry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("form_name", models.SlugField(verbose_name="Form")),
                ("entry_data", models.JSONField(blank=True, default=dict)),
                ("html_headers", models.JSONField(blank=True, default=dict)),
                ("entry_created_at", models.DateTimeField(auto_now_add=True)),
                ("entry_updated_at", models.DateTimeField(auto_now=True)),
                (
                    "form_user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Form entry",
                "verbose_name_plural": "Form entries",
            },
        ),
    ]
