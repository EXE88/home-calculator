# Generated by Django 4.2.4 on 2023-09-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('group', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('last_price', models.CharField(max_length=50)),
            ],
        ),
    ]
