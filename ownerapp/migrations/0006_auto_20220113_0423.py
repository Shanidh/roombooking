# Generated by Django 3.2.7 on 2022-01-13 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0005_alter_ownerproperties_uploadby'),
    ]

    operations = [
        migrations.CreateModel(
            name='facilities',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('free_wifi', models.CharField(max_length=6, null=True)),
                ('restaurant', models.CharField(max_length=6, null=True)),
                ('Room_Service', models.CharField(max_length=6, null=True)),
                ('Bar', models.CharField(max_length=6, null=True)),
                ('front_desk', models.CharField(max_length=6, null=True)),
                ('Sauna', models.CharField(max_length=6, null=True)),
                ('Fitness_Centre', models.CharField(max_length=6, null=True)),
                ('Garden', models.CharField(max_length=6, null=True)),
                ('Terrace', models.CharField(max_length=6, null=True)),
                ('Airport_Shuttle', models.CharField(max_length=6, null=True)),
                ('Family_Rooms', models.CharField(max_length=6, null=True)),
                ('Spa', models.CharField(max_length=6, null=True)),
                ('Hot_Tub', models.CharField(max_length=6, null=True)),
                ('Air_Conditioning', models.CharField(max_length=6, null=True)),
                ('Water_Park', models.CharField(max_length=6, null=True)),
                ('ElectricVehicleChargingStations', models.CharField(max_length=6, null=True)),
                ('Swimming_Pool', models.CharField(max_length=6, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='ownerproperties',
            name='Facilities',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ownerapp.facilities'),
        ),
    ]
