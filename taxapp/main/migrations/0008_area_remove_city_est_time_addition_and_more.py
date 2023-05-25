# Generated by Django 4.2.1 on 2023-05-21 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_routecity_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Локации маршрута',
            },
        ),
        migrations.RemoveField(
            model_name='city',
            name='est_time_addition',
        ),
        migrations.RemoveField(
            model_name='city',
            name='parent_city_id',
        ),
        migrations.AlterUniqueTogether(
            name='route',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='city',
            name='area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='main.area'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='finish_area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='finishing_routes', to='main.area'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='start_area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='starting_routes', to='main.area'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='route',
            unique_together={('start_area', 'finish_area')},
        ),
        migrations.RemoveField(
            model_name='route',
            name='finish_city',
        ),
        migrations.RemoveField(
            model_name='route',
            name='start_city',
        ),
        migrations.DeleteModel(
            name='RouteCity',
        ),
    ]
