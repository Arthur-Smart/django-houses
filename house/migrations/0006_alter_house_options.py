# Generated by Django 4.2 on 2023-04-27 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_house_availability'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ('-created_at',)},
        ),
    ]