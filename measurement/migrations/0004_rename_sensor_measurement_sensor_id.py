# Generated by Django 5.0.6 on 2024-05-28 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_rename_sensor_id_measurement_sensor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor',
            new_name='sensor_id',
        ),
    ]
