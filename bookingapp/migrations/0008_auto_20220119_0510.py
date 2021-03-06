# Generated by Django 3.2.7 on 2022-01-19 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0007_alter_userbooking_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbooking',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='usercontactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=20, null=True)),
                ('message', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bookingapp.userbooking')),
            ],
        ),
    ]
