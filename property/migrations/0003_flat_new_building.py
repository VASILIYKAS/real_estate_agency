# Generated by Django 2.2.24 on 2025-02-11 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20190829_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='new_building',
            field=models.BooleanField(help_text='True — новостройка, False — старое здание,\n        None — не заполнено.', null=True, verbose_name='Новостройка'),
        ),
    ]
