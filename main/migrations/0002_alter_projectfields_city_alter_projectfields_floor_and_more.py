# Generated by Django 4.2.4 on 2023-09-02 16:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectfields',
            name='city',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='projectfields',
            name='floor',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(14), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='projectfields',
            name='roof_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'تیرچه بتنی'), (1, 'تیرچه فولادی')], default=0),
        ),
    ]
