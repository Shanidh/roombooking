# Generated by Django 3.2.7 on 2022-01-16 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0008_remove_ownerproperties_facilities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerproperties',
            name='description',
            field=models.CharField(max_length=5000),
        ),
    ]
