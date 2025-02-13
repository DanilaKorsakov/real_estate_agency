# Generated by Django 2.2.24 on 2024-11-08 10:00
import phonenumbers
from django.db import migrations


def parse_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        owner_pure_phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
        if phonenumbers.is_valid_number(owner_pure_phone):
            flat.owner_pure_phone = owner_pure_phone
            flat.save()



class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(parse_phone)
    ]
