# Generated by Django 3.2.7 on 2022-01-15 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0007_auto_20220115_0054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownerproperties',
            name='Facilities',
        ),
    ]
