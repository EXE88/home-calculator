# Generated by Django 4.2.4 on 2023-09-07 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_projectinputs_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinputs',
            name='build_quality',
            field=models.PositiveSmallIntegerField(choices=[(0, 'استاندارد'), (1, 'خوب'), (2, 'عالی')], default=0),
        ),
    ]
