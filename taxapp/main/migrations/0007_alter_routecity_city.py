# Generated by Django 4.2.1 on 2023-05-20 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_routecity_alter_route_finish_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routecity',
            name='city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='parent_city', to='main.city'),
        ),
    ]
