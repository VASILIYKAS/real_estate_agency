# Generated by Django 2.2.24 on 2025-02-14 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_auto_20250213_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='owner_flats',
            field=models.ManyToManyField(related_name='flats', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
