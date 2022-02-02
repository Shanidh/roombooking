# Generated by Django 3.2.7 on 2022-01-27 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0014_ownercontactus'),
        ('bookingapp', '0009_bookform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookform',
            name='propertyid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ownerapp.ownerproperties'),
        ),
    ]