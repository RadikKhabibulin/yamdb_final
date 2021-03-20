# Generated by Django 3.0.5 on 2020-11-23 20:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201123_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='rating',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
