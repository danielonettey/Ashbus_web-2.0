# Generated by Django 3.2 on 2021-04-16 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashbus_web', '0004_remove_driver_ratings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_trip',
            name='pickup_time',
            field=models.TimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start_time',
            field=models.TimeField(),
        ),
    ]