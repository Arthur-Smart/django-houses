# Generated by Django 4.0.6 on 2023-04-26 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='bedrooms',
            field=models.IntegerField(null=True),
        ),
    ]