# Generated by Django 4.0.6 on 2023-04-26 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_house_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='availability',
            field=models.BooleanField(default=True),
        ),
    ]