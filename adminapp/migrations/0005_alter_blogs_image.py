# Generated by Django 3.2.7 on 2022-01-20 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0004_blogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
