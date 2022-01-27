# Generated by Django 3.2.7 on 2022-01-27 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0014_ownercontactus'),
        ('bookingapp', '0010_alter_bookform_propertyid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookform',
            name='roomid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ownerapp.roomproperty'),
        ),
    ]
