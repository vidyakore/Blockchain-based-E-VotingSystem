# Generated by Django 4.0.3 on 2022-06-14 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booth_manager',
            name='phone_no',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='phone_no',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='voter',
            name='phone_no',
            field=models.CharField(max_length=200),
        ),
    ]
