# Generated by Django 3.2.20 on 2023-07-05 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
