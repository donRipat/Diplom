# Generated by Django 4.2.1 on 2023-06-06 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_remove_booking_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='plate',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='scheduledroute',
            name='time',
            field=models.TimeField(unique=True),
        ),
    ]