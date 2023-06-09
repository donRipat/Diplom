# Generated by Django 4.2.1 on 2023-05-20 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_driver_options_remove_city_dist_parent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteCity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_city', to='main.city', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Маршрутные города',
            },
        ),
        migrations.AlterField(
            model_name='route',
            name='finish_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='finishing_routes', to='main.routecity'),
        ),
        migrations.AlterField(
            model_name='route',
            name='start_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starting_routes', to='main.routecity'),
        ),
    ]
