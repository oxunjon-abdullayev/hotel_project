# Generated by Django 4.2.1 on 2023-08-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_hotelstaff_language_skill_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='person',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='room',
            name='star',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
