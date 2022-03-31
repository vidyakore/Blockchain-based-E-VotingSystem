# Generated by Django 4.0.3 on 2022-03-31 06:53

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0004_booth_manager_candidate_candidate_constituency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booth_manager',
            name='phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='contract_manager',
            name='phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='voter',
            name='phone_no',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=13, region=None, unique=True),
        ),
    ]
