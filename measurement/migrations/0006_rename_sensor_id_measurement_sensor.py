# Generated by Django 4.2.13 on 2024-05-28 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0005_alter_measurement_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
    ]
