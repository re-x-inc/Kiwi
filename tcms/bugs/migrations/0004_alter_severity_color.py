# Generated by Django 4.2.5 on 2023-09-08 09:16

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("bugs", "0003_add_severity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="severity",
            name="color",
            field=colorfield.fields.ColorField(
                default="#FFFFFF", image_field=None, max_length=25, samples=None
            ),
        ),
    ]
