# Generated by Django 4.0.3 on 2022-03-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcontractmanager',
            name='ContractManagerPhone',
            field=models.CharField(max_length=12),
        ),
    ]
