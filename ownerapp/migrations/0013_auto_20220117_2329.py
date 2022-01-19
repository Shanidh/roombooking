# Generated by Django 3.2.7 on 2022-01-18 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0012_roomproperty_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilities',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ownerapp.owners'),
        ),
        migrations.AddField(
            model_name='facilities',
            name='propertyf',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ownerapp.ownerproperties'),
        ),
    ]