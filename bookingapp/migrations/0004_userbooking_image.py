# Generated by Django 3.2.7 on 2022-01-11 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0003_userbooking_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbooking',
            name='image',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
