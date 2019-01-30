# Generated by Django 2.1.5 on 2019-01-30 20:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0004_auto_20190130_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='duration',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Call duration in seconds'),
        ),
    ]
