# Generated by Django 3.2.7 on 2022-01-13 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ownerapp', '0003_alter_owners_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ownerproperties',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('property_name', models.CharField(max_length=50)),
                ('property_type', models.CharField(max_length=20, null=True)),
                ('star_rate', models.CharField(max_length=20, null=True)),
                ('contact_name', models.CharField(max_length=50)),
                ('contact_phone', models.BigIntegerField()),
                ('property_address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=20, null=True)),
                ('State', models.CharField(max_length=20, null=True)),
                ('Pincode', models.CharField(max_length=6)),
                ('description', models.CharField(max_length=500)),
                ('Cancel_freecharge_date', models.CharField(max_length=20, null=True)),
                ('Children', models.CharField(max_length=20, null=True)),
                ('pets', models.CharField(max_length=20, null=True)),
                ('payment', models.CharField(max_length=20, null=True)),
                ('uploadby', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ownerapp.owners')),
            ],
        ),
    ]
