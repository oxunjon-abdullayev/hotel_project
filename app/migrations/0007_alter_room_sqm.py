# Generated by Django 4.2.1 on 2023-08-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_room_price_room_sqm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='sqm',
            field=models.FloatField(default=12),
        ),
    ]
