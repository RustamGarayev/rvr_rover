# Generated by Django 3.2.12 on 2022-04-24 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_sensorreading_temperature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensorreading',
            old_name='no2_level_in_ppm',
            new_name='n2_level_in_ppm',
        ),
    ]
