# Generated by Django 4.2.1 on 2023-05-23 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_passenger_est_dep_time_alter_city_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='max_time',
            new_name='time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='min_time',
        ),
    ]
