# Generated by Django 2.2.24 on 2025-02-12 12:53

import phonenumbers
from django.db import migrations


def standardized_phone_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')

    for flat in Flat.objects.iterator(chunk_size=200):
        phone_number = flat.phonenumber

        if not phone_number or not phonenumbers.is_valid_number(
                phonenumbers.parse(phone_number, 'RU')):
            flat.pure_phone = None
            flat.save()

        else:
            parse_phone_number = phonenumbers.parse(phone_number, 'RU')
            flat.pure_phone = phonenumbers.format_number(
                parse_phone_number, phonenumbers.PhoneNumberFormat.E164)
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(standardized_phone_number)
    ]
